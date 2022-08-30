import cv2
import numpy as np
import pandas as pd
import os

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
    df = pd.DataFrame({
        "R" : R,
        "G" : G,
        "B" : B,
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