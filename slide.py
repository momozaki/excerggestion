import glob
import os
import cv2
import numpy as np

imagePath="./images/*"

files=[os.path.basename(f) for f in glob.glob(imagePath,recursive=True)
if os.path.isfile(f)]#imagesフォルダのファイル名のみを取り出す

for number,file in enumerate(files):
    img=cv2.imread("./images/{}".format(file))#画像読み込み

    #サイズ決定
    h=img.shape[0]
    w=img.shape[1]
    #平行移動の値 100pxずつ
    x,y=100,100
    # 平行移動の変換行列を作成
    afin_matrix=np.float32([1,0,x],[0,1,y])

    # アファイン変換適用     
    afin_img=cv2.warpAffine(img,
    afin_matrix,
    (h,w))

# 画像表示
cv2.imshow("img",afin_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


