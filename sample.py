import numpy as np               #version 1.14.3
import matplotlib.pyplot as plt 
from skimage import io           #scikit image version 0.13.1
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 12

def gammma(x, r):
    """
    ガンマ補正y=255*(x/255) 
    x 入力画像
    r ガンマ補正の係数
    """
    x = np.float64(x)
    y = x/255.
    y = y **(1/r)
    return np.uint8(255*y)

def hist_rgb(img):
    #rgbのヒストグラムを作成する関数
    #結果を格納する変数res [brightness, channel]
    res = np.zeros([256, 3])   
    for channel in range(3):
        #あるchannelを抽出
        img_tmp = img[:,:,channel]
        #画像を1次元にする
        img_tmp =img_tmp.reshape(img_tmp.size)
        for i in img_tmp:
            res[i, channel] += 1
    return res

def mat_hist_rgb(hist, ylim = 0.06):
    #hist_rgbのfunctionで計算したヒストグラムを表示
    x = np.arange(hist.shape[0])
    #ヒストグラムの色を指定
    colors = ["red", "green", "blue"]
    for i, color in enumerate(colors):
        plt.bar(x,hist[:, i], color=color, alpha=0.3, width=1.0)
    plt.xlabel("Brightness")
    plt.ylabel("Frequency")
    plt.xlim(0, 255)
    plt.yticks([])
    plt.show()

img_lena = io.imread("chart_1_input.tif")
img_gamma = gammma(img_lena, r=0.5)
#io.imsave("r05.png", img_gamma)
#mat_hist_rgb(hist_rgb(img_gamma))