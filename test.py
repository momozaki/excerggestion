import glob
import os
import cv2
import numpy as np
from PIL import Image
import os

imagePath="./images/*"
"""
#日本語のファイルを開くための処理
for before in befores:
    pil_img=Image.open(before) #Pillowで画像ファイルを開く
    img=np.array(pil_img)#Pillowからnumpyへ変換
    if img.ndim==3:
        img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""

files=[os.path.basename(f) for f in glob.glob("./images/*",recursive=True)
if os.path.isfile(f)]#imagesフォルダのファイルを取り出す

for number,file in enumerate(files):
    img=cv2.imread("./images/{}".format(file))#絶対パスのみ
    (h,w)=img.shape[:2]
    center=(w/2,h/2)
    angle=-150
    scale=1
    M=cv2.getRotationMatrix2D(center,angle,scale)
    img_rotate=cv2.warpAffine(img,M,(w,h))

    cv2.imshow('original Image', img)
    cv2.imshow('Rotated Image', img_rotate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("./rotated_30_image/30-{}-{}".format(number,file),img_rotate)#30
    

