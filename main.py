# やるべきことは簡潔に無駄なことはしない
import pandas as pd

def InputData(path):
    print("Detect Input Data")


def Gamma1(param):
    print("###GAMMA 1###")
    print("\t--",param)

    #ROUND(255*(A4/255)^$G$3,0)

if __name__ == "__main__":

    gamma1_param = [0.1 , 0.2 , 0.3 , 0.4 , 0.5 , 0.6 , 0.7 ,0.8]
    for i in gamma1_param:
        Gamma1(i)