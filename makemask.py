#from readline import append_history_file
import cv2
import numpy as np
import pandas as pd
import os
from skimage import io, color

def makecirkle(X,Y):
    cv2.circle(img,
           center=(X, Y),
           radius=50,
           color=(0, 255, 0),
           thickness=3,
           lineType=cv2.LINE_4,
           shift=0)
def makecirkle_Y(X,Y):
    cv2.circle(img,
        center=(X, Y),
        radius=50,
        color=(0, 255, 0),
        thickness=3,
        lineType=cv2.LINE_4,
        shift=0)

def con2Lab(B,G,R):
    L = []
    a = []
    b = []
    for i in range(len(B)):
        if R[i]/255 <= 0.040450:
            R_ = R[i]/255/12.92
        else:
            R_ = ((R[i]/255+0.055)/1.055)**(2.4)
        if G[i]/255 <= 0.040450:
            G_ = G[i]/255/12.92
        else:
            G_ = ((G[i]/255+0.055)/1.055)**(2.4)
        if B[i]/255 <= 0.040450:
            B_ = B[i]/255/12.92
        else:
            B_ = ((B[i]/255+0.055)/1.055)**(2.4)

        X=0.4124*R_+0.3576*G_+0.1805*B_
        Y=0.2126*R_+0.7152*G_+0.0722*B_
        Z=0.0193*R_+0.1192*G_+0.9505*B_

        Xn = 0.9504
        Yn = 1
        Zn = 1.0889

        if X/Xn > (6/29)**3:
            fX = (X/Xn)**(1/3)
        else:
            fX = (1/3)*((29/6)**2)*(X/Xn)+(4/29)
        if Y/Yn > (6/29)**3:
            fY = (Y/Yn)**(1/3)
        else:
            fY = (1/3)*((29/6)**2)*(Y/Yn)+(4/29)
        if Z/Zn > (6/29)**3:
            fZ = (Z/Zn)**(1/3)
        else:
            fZ = (1/3)*((29/6)**2)*(Z/Zn)+(4/29)
        
        L_i = 116*fY - 16
        a_i = 500*(fX-fY)
        b_i = 200*(fY-fZ)

        L.append(L_i)
        a.append(a_i)
        b.append(b_i)
    df_Lab = pd.DataFrame({
        "L" : L,
        "a" : a,
        "b" : b,
    })
    return df_Lab





def conv2RGB(img):
    #img = cv2.imread('chart_1_input.tif')
    init_X = 240
    init_Y = 280

    annotaion_list = []

    f_X = init_X
    f_Y = init_Y

    for i in range(5):
        frag = 0
        X2Y = []
        makecirkle(init_X , init_Y)
        X2Y.append(init_X)
        X2Y.append(init_Y)
        annotaion_list.append(X2Y)
        for j in range(25):
            X2Y = []
            makecirkle_Y(f_X , f_Y)
            if frag == 0:
                frag = 1
            else:
                X2Y.append(f_X)
                X2Y.append(f_Y)
                annotaion_list.append(X2Y)
            f_Y += 178
        f_X += 170
        f_Y = init_Y
        init_X += 170



    sec_X = 1130
    f_X = 1130
    for i in range(5):
        frag = 0
        X2Y = []
        makecirkle(sec_X , init_Y)
        X2Y.append(sec_X)
        X2Y.append(init_Y)
        annotaion_list.append(X2Y)
        for j in range(25):
            X2Y = []
            makecirkle_Y(f_X , f_Y)
            if frag == 0:
                frag = 1
            else:
                X2Y.append(f_X)
                X2Y.append(f_Y)
                annotaion_list.append(X2Y)
            f_Y += 178
        f_X += 170
        f_Y = init_Y
        init_X += 170


    sep_X = 1130 + 880
    f_X = 1130 + 880
    for i in range(5):
        frag = 0
        X2Y = []
        makecirkle(sep_X , init_Y)
        X2Y.append(init_X)
        X2Y.append(init_Y)
        annotaion_list.append(X2Y)
        for j in range(25):
            X2Y = []
            makecirkle_Y(f_X , f_Y)
            if frag == 0:
                frag = 1
            else:
                X2Y.append(f_X)
                X2Y.append(f_Y)
                annotaion_list.append(X2Y)
            f_Y += 178
        f_X += 170
        f_Y = init_Y
        init_X += 170

    sep_X +=  880
    f_X = sep_X
    for i in range(5):
        frag = 0
        X2Y = []
        makecirkle(sep_X , init_Y)
        X2Y.append(init_X)
        X2Y.append(init_Y)
        annotaion_list.append(X2Y)
        for j in range(25):
            X2Y = []
            makecirkle_Y(f_X , f_Y)
            if frag == 0:
                frag = 1
            else:
                X2Y.append(f_X)
                X2Y.append(f_Y)
                annotaion_list.append(X2Y)
            f_Y += 178
        f_X += 170
        f_Y = init_Y
        init_X += 170

    sep_X +=  900
    f_X = sep_X
    for i in range(5):
        frag = 0
        X2Y = []
        makecirkle(sep_X , init_Y)
        X2Y.append(init_X)
        X2Y.append(init_Y)
        annotaion_list.append(X2Y)
        for j in range(25):
            X2Y = []
            makecirkle_Y(f_X , f_Y)
            if frag == 0:
                frag = 1
            else:
                X2Y.append(f_X)
                X2Y.append(f_Y)
                annotaion_list.append(X2Y)
            f_Y += 178
        f_X += 170
        f_Y = init_Y
        init_X += 170

    sep_X +=  900
    f_X = sep_X
    for i in range(5):
        frag = 0
        X2Y = []
        makecirkle(sep_X , init_Y)
        X2Y.append(init_X)
        X2Y.append(init_Y)
        annotaion_list.append(X2Y)
        for j in range(26):
            X2Y = []
            makecirkle_Y(f_X , f_Y)
            if frag == 0:
                frag = 1
            else:
                X2Y.append(f_X)
                X2Y.append(f_Y)
                annotaion_list.append(X2Y)
            f_Y += 178
        f_X += 170
        f_Y = init_Y
        init_X += 170

    sep_X +=  890
    f_X = sep_X
    for i in range(8):
        frag = 0
        X2Y = []
        makecirkle(sep_X , init_Y)
        X2Y.append(init_X)
        X2Y.append(init_Y)
        annotaion_list.append(X2Y)
        for j in range(26):
            X2Y = []
            makecirkle_Y(f_X , f_Y)
            if frag == 0:
                frag = 1
            else:
                X2Y.append(f_X)
                X2Y.append(f_Y)
                annotaion_list.append(X2Y)
            f_Y += 178
        f_X += 170
        f_Y = init_Y
        init_X += 170

    # 963points
    R = []
    G = []
    B = []
    for point in annotaion_list:
        boxFromX = point[0] #対象範囲開始位置 X座標
        boxFromY = point[1] #対象範囲開始位置 Y座標
        boxToX = point[0]+2 #対象範囲終了位置 X座標
        boxToY = point[1]+2 #対象範囲終了位置 Y座標
        # y:y+h, x:x+w　の順で設定
        # 青、緑、赤
        imgBox = img[boxFromY:boxToY, boxFromX:boxToX]
        b = imgBox.T[0].flatten().mean()
        g = imgBox.T[1].flatten().mean()
        r = imgBox.T[2].flatten().mean()

        # RGB平均値を取得
        #print("B: %.2f" % (b))
        #print("G: %.2f" % (g))
        #print("R: %.2f" % (r))

        R.append(int(r))
        G.append(int(g))
        B.append(int(b))
    df_Lab = con2Lab(B,G,R)
    df = pd.DataFrame({
        "R" : R,
        "G" : G,
        "B" : B,
        "L" : df_Lab["L"],
        "a" : df_Lab["a"],
        "b" : df_Lab["b"],
    })
    df.to_csv(savepath + "/point_rbf.csv")

    #cv2.imwrite('opencv-line-01.jpg', img)


# ここから書いたらOK
init_path = os.getcwd()

gamma1_path = init_path + "/Gamma1"
gamma1_param = [0.1 , 0.2 , 0.3 , 0.4 , 0.5 , 0.6 , 0.7 ,0.8]
for i in gamma1_param:
    img_path = gamma1_path + "/" + str(i)
    img = cv2.imread(img_path+'/output.bmp')
    savepath = gamma1_path + "/" + str(i)
    conv2RGB(img)
print("###FIN GAMMA1###")


gamma2_path = init_path + "/gamma2"
gamma2_param = [0.5 , 0.7 , 0.8 , 0.9 , 1.0 , 1.1 , 1.2 ,1.3]
for i in gamma2_param:
    img_path = gamma2_path + "/" + str(i)
    img = cv2.imread(img_path+'/output.bmp')
    savepath = gamma2_path + "/" + str(i)
    conv2RGB(img)
print("###FIN GAMMA2###")


gamma3_path = init_path + "/gamma3"
gamma3_param1 = [0.2 , 0.3 , 0.4 , 0.5 , 0.6 , 0.7 , 0.8 , 0.9]
gamma3_param2 = [0.224 , 0.336 , 0.448 , 0.56 , 0.672 , 0.784 , 0.896 ,1.008]
count = 0
for i in gamma3_param1:
    img_path = gamma3_path + "/" + str(i)
    img = cv2.imread(img_path+'/output.bmp')
    savepath = gamma3_path + "/" + str(i)
    conv2RGB(img)
print("###FIN GAMMA3###")