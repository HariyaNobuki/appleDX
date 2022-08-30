# やるべきことは簡潔に無駄なことはしない
import os , sys
import pandas as pd

def InputData(path):
    print("Detect Input Data")
    df = pd.read_csv(path)
    #R = df["R"]
    #G = df["G"]
    #B = df["B"]
    return df

# return is Output Dict
def Gamma1(input_dict,param):
    df_output = pd.DataFrame()
    print("###GAMMA 1###")
    print("\t--",param)
    
    return df_output
    a=0

    #ROUND(255*(A4/255)^$G$3,0)

if __name__ == "__main__":
    init_path = os.getcwd()
    input_path = init_path + "/input_data.csv"
    input_dict = InputData(input_path)

    gamma1_param = [0.1 , 0.2 , 0.3 , 0.4 , 0.5 , 0.6 , 0.7 ,0.8]
    for i in gamma1_param:
        Gamma1(input_dict,i)