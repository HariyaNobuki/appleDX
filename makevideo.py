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
    size=(900,600)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    save = cv2.VideoWriter('gamma1.avi',fourcc,70,size)#動画を保存する形を作成

    makefiles(init_path,"Gamma1")
    gamma1_path = init_path + "/Gamma1"
    gamma1_param = [0.01*i for i in range(500)]
    gamma1_param = np.round(gamma1_param , 2)

    for i in gamma1_param:
        img=gamma1_path+"/"+str(i)+"/output.bmp"
        img=cv2.imread(img)
        img=cv2.resize(img,size)
        save.write(img)
    
    save.release()

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    save = cv2.VideoWriter('gamma2.avi',fourcc,70,size)#動画を保存する形を作成

    makefiles(init_path,"Gamma2")
    gamma1_path = init_path + "/Gamma2"
    gamma1_param = [0.01*i for i in range(500)]
    gamma1_param = np.round(gamma1_param , 2)

    for i in gamma1_param:
        img=gamma1_path+"/"+str(i)+"/output.bmp"
        img=cv2.imread(img)
        img=cv2.resize(img,size)
        save.write(img)
    
    save.release()

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    save = cv2.VideoWriter('gamma3.avi',fourcc,70,size)#動画を保存する形を作成

    makefiles(init_path,"Gamma3")
    gamma1_path = init_path + "/Gamma3"
    gamma1_param = [0.01*i for i in range(500)]
    gamma1_param = np.round(gamma1_param , 2)

    for i in gamma1_param:
        img=gamma1_path+"/"+str(i)+"/output.bmp"
        img=cv2.imread(img)
        img=cv2.resize(img,size)
        save.write(img)
    
    save.release()