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

def makehistgram(df_data):
    print("### makehist")
    if gamma_num == 1:
        fig = plt.figure(figsize=(12,6))
        for par in gamma1_param:
            if par == 1.8:
                plt.hist(df_data["{}".format(par)],bins=100,alpha=0.5,histtype='stepfilled',label=par,color="r")
            else:
                plt.hist(df_data["{}".format(par)],bins=100,alpha=0.15,histtype='stepfilled',label=par)
        plt.xlabel("error",fontsize=20)
        plt.ylabel("frepuency",fontsize=20)
        plt.xlim(0,80)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.rc("legend",fontsize=15)
        plt.legend()
        fig.savefig(gamma_path+"/summary_hist.png")
    elif gamma_num == 2:
        fig = plt.figure(figsize=(12,6))
        for par in gamma1_param:
            if par == 0.2:
                plt.hist(df_data["{}".format(par)],bins=100,alpha=0.5,histtype='stepfilled',label=par,color="r")
            else:
                plt.hist(df_data["{}".format(par)],bins=100,alpha=0.15,histtype='stepfilled',label=par)
        plt.xlabel("error",fontsize=20)
        plt.ylabel("frepuency",fontsize=20)
        plt.xlim(0,80)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.rc("legend",fontsize=15)
        plt.legend()
        fig.savefig(gamma_path+"/summary_hist.png")
    elif gamma_num == 3:
        fig = plt.figure(figsize=(12,6))
        for par in gamma1_param:
            if par == 1.2:
                plt.hist(df_data["{}".format(par)],bins=100,alpha=0.5,histtype='stepfilled',label=par,color="r")
            else:
                plt.hist(df_data["{}".format(par)],bins=100,alpha=0.15,histtype='stepfilled',label=par)
        plt.xlabel("error",fontsize=20)
        plt.ylabel("frepuency",fontsize=20)
        plt.xlim(0,120)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.rc("legend",fontsize=15)
        plt.legend()
        fig.savefig(gamma_path+"/summary_hist.png")


if __name__ == "__main__":
    print("###compare###")
    init_path = os.getcwd()
    input_Lab = pd.read_csv(init_path + "/point_rbf_input.csv")
    target_Lab = pd.read_csv(init_path + "/point_rbf_target.csv")

    df_E_mean = pd.DataFrame()

    input_E = CompareLab(input_Lab)
    makepic(input_E,init_path)
    ErrorAnalysis = anaE(input_E)

    df_hist = pd.DataFrame()    # for histgram
    gamma1_path = init_path + "/Gamma1"
    gamma_path = init_path + "/Gamma1"
    gamma_num =  1
    gamma1_param =[0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8]
    for i in gamma1_param:
        savepath = gamma1_path + "/" + str(i)
        com_Lab = pd.read_csv(savepath + "/point_rbf.csv")
        com_E = CompareLab(com_Lab)
        makepic(com_E,savepath)
        df_hist["{}".format(i)] = com_E
        E_mean = anaE(com_E)
        df_E_mean["gamma1_{}".format(i)] = [E_mean]
    makehistgram(df_hist)
    print("###FIN GAMMA1###")

    df_hist = pd.DataFrame()    # for histgram
    gamma2_path = init_path + "/gamma2"
    gamma_path = init_path + "/Gamma2"
    gamma_num =  2
    gamma2_param = [0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8]
    for i in gamma2_param:
        savepath = gamma2_path + "/" + str(i)
        com_Lab = pd.read_csv(savepath + "/point_rbf.csv")
        com_E = CompareLab(com_Lab)
        makepic(com_E,savepath)
        df_hist["{}".format(i)] = com_E
        E_mean = anaE(com_E)
        df_E_mean["gamma2_{}".format(i)] = [E_mean]
    makehistgram(df_hist)
    print("###FIN gamma2###")

    #df_hist = pd.DataFrame()    # for histgram
    #gamma3_path = init_path + "/gamma3"
    #gamma_path = init_path + "/Gamma3"
    #gamma_num =  3
    #gamma3_param1 = [0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8]
    #gamma3_param2 = [0.224,0.448,0.672,0.896 ,1.008,1.344,1.568,1.792,2.016]
    #for i in gamma3_param1:
    #    savepath = gamma3_path + "/" + str(i)
    #    com_Lab = pd.read_csv(savepath + "/point_rbf.csv")
    #    com_E = CompareLab(com_Lab)
    #    makepic(com_E,savepath)
    #    df_hist["{}".format(i)] = com_E
    #    E_mean = anaE(com_E)
    #    df_E_mean["gamma3_{}".format(i)] = [E_mean]
    #makehistgram(df_hist)
    #print("###FIN gamma3###")

    df_E_mean.to_csv("Errors.csv")