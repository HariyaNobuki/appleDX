import cv2
import glob
import os , sys
import numpy as np

def makefiles(path,filename):
    os.makedirs(path + "/" + filename ,exist_ok=True)

if __name__ == "__main__":
    init_path = os.getcwd()
    bat_file = "\n"

    # Gamma1
    size=(1200,901)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    save = cv2.VideoWriter('gamma1.avi',fourcc,70,size)#動画を保存する形を作成

    makefiles(init_path,"Gamma1")
    gamma1_path = init_path + "/Gamma1"
    gamma1_param = [0.01*i for i in range(500)]
    gamma1_param = np.round(gamma1_param , 2)
    for i in gamma1_param:
        img = cv2.imread(gamma1_path+"/"+str(i)+"/output.bmp")
        cv2.putText(img, 'gamma={}'.format(i), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 5, cv2.LINE_AA)
        cv2.imwrite(gamma1_path+"/"+str(i)+"/output_txt.bmp", img)

    makefiles(init_path,"Gamma2")
    gamma2_path = init_path + "/Gamma2"
    gamma2_param = [0.01*i for i in range(500)]
    gamma2_param = np.round(gamma2_param , 2)
    for i in gamma2_param:
        img = cv2.imread(gamma2_path+"/"+str(i)+"/output.bmp")
        cv2.putText(img, 'gamma={}'.format(i), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 5, cv2.LINE_AA)
        cv2.imwrite(gamma2_path+"/"+str(i)+"/output_txt.bmp", img)

    makefiles(init_path,"Gamma3")
    gamma3_path = init_path + "/Gamma3"
    gamma3_param = [0.01*i for i in range(500)]
    gamma3_param = np.round(gamma3_param , 2)
    for i in gamma3_param:
        img = cv2.imread(gamma3_path+"/"+str(i)+"/output.bmp")
        cv2.putText(img, 'gamma={}'.format(i), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 5, cv2.LINE_AA)
        cv2.imwrite(gamma3_path+"/"+str(i)+"/output_txt.bmp", img)