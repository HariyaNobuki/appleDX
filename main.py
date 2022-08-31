# if_gamma
import os , sys
import pandas as pd
import numpy as np
import cv2

def makefiles(path,filename):
    os.makedirs(path + "/" + filename ,exist_ok=True)


def InputData(path):
    print("Detect Input Data")
    df = pd.read_csv(path)
    return df

def sep_space(df):
    txtstring = str(df["R"][0]) + " " + str(df["G"][0]) + " " + str(df["B"][0]) + "\n"
    for i in range(len(df)):
        if i >= 1:
            txtstring += str(df["R"][i]) + " " + str(df["G"][i]) + " " + str(df["B"][i]) + "\n"
    f = open(savepath + "/conv_RBF.txt", "w")
    f.write(txtstring)
    f.close()



# return is not , but save performance
def Gamma1(input_dict,param):
    RGB = ["R","G","B"]
    max_format = 255
    df_output = pd.DataFrame()
    print("###GAMMA 1###")
    print("\t--",param)
    for c in RGB:
        color = np.array(input_dict["{}".format(c)])
        o_color = np.trunc(max_format*(color/max_format)**param).astype("int")
        df_output["{}".format(c)] = o_color
    df_output.to_csv(savepath + "/conv_RBF.csv")
    sep_space(df_output)


def Gamma2(input_dict,param):
    RGB = ["R","G","B"]
    max_format = 255
    df_output = pd.DataFrame()
    print("###GAMMA 1###")
    print("\t--",param)
    for c in RGB:
        color = np.array(input_dict["{}".format(c)])
        o_color = np.trunc(max_format*(1-color/max_format)**param).astype("int")
        df_output["{}".format(c)] = o_color
    df_output.to_csv(savepath + "/conv_RBF.csv")
    sep_space(df_output)

def Gamma3(input_dict,param1,param2):
    RGB = ["R","G","B"]
    max_format = 255
    df_output = pd.DataFrame()
    print("###GAMMA 1###")
    print("\t--",param1,param2)
    for c in RGB:
        color = np.array(input_dict["{}".format(c)])
        o_color = np.trunc(max_format-max_format*(1-(color/max_format)**param1)**param2).astype("int")
        df_output["{}".format(c)] = o_color
    df_output.to_csv(savepath + "/conv_RBF.csv")
    sep_space(df_output)


if __name__ == "__main__":
    init_path = os.getcwd()
    input_path = init_path + "/input_data.csv"
    input_dict = InputData(input_path)
    bat_file = "\n"


    makefiles(init_path,"Gamma1")
    gamma1_path = init_path + "/Gamma1"
    gamma1_param = [0.1 , 0.2 , 0.3 , 0.4 , 0.5 , 0.6 , 0.7 ,0.8, 0.9]
    for i in gamma1_param:
        makefiles(gamma1_path,str(i))
        savepath = gamma1_path + "/" + str(i)
        Gamma1(input_dict,i)
        bat_file += "convert_color.exe chart_6_input-col.tif "+savepath+"/output.bmp "+savepath+"/conv_RBF.txt\n"
    print("###FIN GAMMA1###")

    makefiles(init_path,"Gamma2")
    gamma2_path = init_path + "/gamma2"
    gamma2_param = [1.1,1.2,1.3,1.4,1.5,1.6]
    for i in gamma2_param:
        makefiles(gamma2_path,str(i))
        savepath = gamma2_path + "/" + str(i)
        Gamma2(input_dict,i)
        bat_file += "convert_color.exe chart_6_input-col.tif "+savepath+"/output.bmp "+savepath+"/conv_RBF.txt\n"
    print("###FIN GAMMA2###")

    makefiles(init_path,"Gamma3")
    gamma3_path = init_path + "/gamma3"
    gamma3_param1 = [0.2 , 0.3 , 0.4 , 0.5 , 0.6 , 0.7 , 0.8 , 0.9,2.0]
    gamma3_param2 = [0.224 , 0.336 , 0.448 , 0.56 , 0.672 , 0.784 , 0.896 ,1.008,2.4]

    count = 0
    for i in gamma3_param1:
        makefiles(gamma3_path,str(i))
        savepath = gamma3_path + "/" + str(i)
        Gamma3(input_dict,gamma3_param1[count],gamma3_param2[count])
        bat_file += "convert_color.exe chart_6_input-col.tif "+savepath+"/output.bmp "+savepath+"/conv_RBF.txt\n"
        count+=1
    print("###FIN gamma3###")
    f = open(init_path + "/henkan.txt", "w")
    f.write(bat_file)
    f.close()

