import cv2
import numpy as np
import pandas as pd
import os
from skimage import io, color
import matplotlib.pyplot as plt
import statistics

from main import makefiles


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

    fig = plt.figure(figsize=(12,6))
    for par in mix_par:
        if par == 0.1:
            df_final["final"] = df_data["{}".format(par)]
            plt.hist(df_data["{}".format(par)],bins=100,alpha=0.5,histtype='stepfilled',label=par,color="r")
        else:
            plt.hist(df_data["{}".format(par)],bins=100,alpha=0.15,histtype='stepfilled',label=par)
    plt.xlabel("error",fontsize=20)
    plt.ylabel("frepuency",fontsize=20)
    plt.xlim(0,50)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.rc("legend",fontsize=15)
    plt.legend()
    fig.savefig(mixer_path+"/summary_hist.png")

def makehistgram_fin(df_data):
    print("### makehist")
    fig = plt.figure(figsize=(12,6))
    plt.hist(df_data["input"],bins=100,alpha=0.3,histtype='stepfilled',label="input")
    plt.hist(df_data["final"],bins=100,alpha=0.3,histtype='stepfilled',label="ours")
    plt.xlabel("error",fontsize=20)
    plt.ylabel("frepuency",fontsize=20)
    plt.xlim(0,60)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.rc("legend",fontsize=15)
    plt.legend()
    fig.savefig(savepath+"/summary_hist.png")


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
    mixer_path = init_path + "/_mixer"

    mix_par = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    df_final = pd.DataFrame()
    for i in mix_par:
        savepath = mixer_path + "/" + str(i)
        com_Lab = pd.read_csv(savepath + "/point_rbf.csv")
        com_E = CompareLab(com_Lab)
        makepic(com_E,savepath)
        df_hist["{}".format(i)] = com_E
        E_mean = anaE(com_E)
        df_E_mean["mixer_{}".format(i)] = [E_mean]
    makehistgram(df_hist)
    print("###FIN MIXER###")

    df_E_mean.to_csv(mixer_path +"/Errors.csv")

    df_hist = pd.DataFrame()    # for histgram
    print("### Last Phase ###")
    makefiles(init_path,"_final")
    savepath = init_path+"/_final"
    com_E = CompareLab(input_Lab)
    E_mean = anaE(com_E)
    df_hist["input"] = com_E
    df_hist["final"] = df_final["final"]
    makehistgram_fin(df_hist)
    print("###ALL FIN###")