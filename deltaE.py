import cv2
import numpy as np
import pandas as pd
import os
from skimage import io, color
import matplotlib.pyplot as plt
import statistics


def CompareLab(com_data):
    L = target_Lab["L"]
    a = target_Lab["a"]
    b = target_Lab["b"]
    L_ = com_data["L"]
    a_ = com_data["a"]
    b_ = com_data["b"]
    E = ((L-L_)**2 + (a-a_)**2 + (b-b_)**2)**(0.5)
    return E

def anaE(Error):
    return statistics.mean(Error)

def makepic(E,savepath):
    fig = plt.figure()
    plt.hist(E,color= 'c',alpha=0.5)
    plt.xlim(0,60)
    plt.ylim(0,300)
    plt.xlabel("Error")
    plt.ylabel("Frequency")
    fig.savefig(savepath+"/hist.png")


if __name__ == "__main__":
    print("###compare###")
    init_path = os.getcwd()
    input_Lab = pd.read_csv(init_path + "/point_rbf_input.csv")
    target_Lab = pd.read_csv(init_path + "/point_rbf_target.csv")

    df_E_mean = pd.DataFrame()

    input_E = CompareLab(input_Lab)
    makepic(input_E,init_path)
    ErrorAnalysis = anaE(input_E)

    gamma1_path = init_path + "/Gamma1"
    gamma1_param = [0.1 , 0.2 , 0.3 , 0.4 , 0.5 , 0.6 , 0.7 ,0.8,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8]

    for i in gamma1_param:
        savepath = gamma1_path + "/" + str(i)
        com_Lab = pd.read_csv(savepath + "/point_rbf.csv")
        com_E = CompareLab(com_Lab)
        makepic(com_E,savepath)
        E_mean = anaE(com_E)
        df_E_mean["gamma1_{}".format(i)] = [E_mean]
    print("###FIN GAMMA1###")


    gamma2_path = init_path + "/gamma2"
    gamma2_param = [0.2,0.3,0.4,0.5,0.7,0.8,0.9,1.0,1.1,1.2,1.3]
    for i in gamma2_param:
        savepath = gamma2_path + "/" + str(i)
        com_Lab = pd.read_csv(savepath + "/point_rbf.csv")
        com_E = CompareLab(com_Lab)
        makepic(com_E,savepath)
        E_mean = anaE(com_E)
        df_E_mean["gamma2_{}".format(i)] = [E_mean]
    print("###FIN gamma2###")

    gamma3_path = init_path + "/gamma3"
    gamma3_param1 = [0.2 , 0.3 , 0.4 , 0.5 , 0.6 , 0.7 , 0.8 , 0.9,2.0]
    gamma3_param2 = [0.224 , 0.336 , 0.448 , 0.56 , 0.672 , 0.784 , 0.896 ,1.008,2.4]
    for i in gamma3_param1:
        savepath = gamma3_path + "/" + str(i)
        com_Lab = pd.read_csv(savepath + "/point_rbf.csv")
        com_E = CompareLab(com_Lab)
        makepic(com_E,savepath)
        E_mean = anaE(com_E)
        df_E_mean["gamma3_{}".format(i)] = [E_mean]
    print("###FIN gamma3###")

    df_E_mean.to_csv("Errors.csv")