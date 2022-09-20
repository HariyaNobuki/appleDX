import matplotlib.pyplot as plt
import numpy as plt 
import pandas as pd
import numpy as np
import os

def makefiles(path,filename):
    os.makedirs(path + "/" + filename ,exist_ok=True)

def mixer(input_df_1,input_df_2,par):
    print("### PAR ###",par)
    par1 = par
    par2 = 1 - par1
    df_mixed = pd.DataFrame()
    R1 = input_df_1["R"]
    R2 = input_df_2["R"]
    G1 = input_df_1["G"]
    G2 = input_df_2["G"]
    B1 = input_df_1["B"]
    B2 = input_df_2["B"]
    df_mixed["R"] = np.trunc(par1*R1 + par2*R2).astype(int)
    df_mixed["G"] = np.trunc(par1*G1 + par2*G2).astype(int)
    df_mixed["B"] = np.trunc(par1*B1 + par2*B2).astype(int)
    return df_mixed

def sep_space(df):
    txtstring = str(df["R"][0]) + " " + str(df["G"][0]) + " " + str(df["B"][0]) + "\n"
    for i in range(len(df)):
        if i >= 1:
            txtstring += str(df["R"][i]) + " " + str(df["G"][i]) + " " + str(df["B"][i]) + "\n"
    f = open(savepath + "/conv_RBF.txt", "w")
    f.write(txtstring)
    f.close()


if __name__ == "__main__":
    print("###This is Mixer###")
    bat_file = "\n"
    
    init_path = os.getcwd()
    mixer_path = init_path + "/_mixer"

    df_gamma = pd.read_csv(mixer_path + "/conv_RBF_gamma.csv")
    df_HSV = pd.read_csv(mixer_path + "/conv_RGB_HSV.csv")

    input_Lab = pd.read_csv(init_path + "/point_rbf_input.csv")
    target_Lab = pd.read_csv(init_path + "/point_rbf_target.csv")

    mix_par = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    df_mixer = pd.DataFrame()
    for par in mix_par:
        makefiles(mixer_path,"{}".format(par))
        df_mixer = mixer(df_gamma,df_HSV,par)
        savepath = mixer_path + "/" + str(par)
        df_mixer.to_csv(savepath+"/conv_RBF.csv")
        sep_space(df_mixer)
        bat_file += "convert_color.exe chart_1_input.tif "+savepath+"/output.bmp "+savepath+"/conv_RBF.txt\n"
    print("###FIN###")
    f = open(init_path + "/mixer.txt", "w")
    f.write(bat_file)
    f.close()

