import glob
import os
import cv2
import numpy as np

class slide:

    imagePath="./images/*"

    files=[os.path.basename(f) for f in glob.glob(imagePath,recursive=True)
    if os.path.isfile(f)]#imagesフォルダのファイル名のみを取り出す


    dir="./edited_slide"
    countdir=(sum(os.path.isdir(os.path.join(dir, name)) for name in os.listdir(dir)))
        #edited_slideのフォルダの数

    #写真を入れるためのフォルダを作る
    if countdir<2:
        os.makedirs("./edited_slide/slided_x_300_y_300_image",exist_ok=True)
        os.makedirs("./edited_slide/slided_x_-300_y_-300_image",exist_ok=True)
            
    #x=300y=300までを出力する処理
    for file in files:

        #画像読込
        img = cv2.imread(f"./images/{file}")

        # 画像サイズ
        height = img.shape[0]  # 高さ
        width  = img.shape[1]  # 幅

        #画像をpxずつ並行移動0,0が真ん中yは-で上に行く
        for x in range(0,301,20):
            for y in range(0,301,20):


                # 平行移動の変換行列を作成
                afin_matrix = np.float32([[1,0,x],[0,1,y]])

                # アファイン変換適用
                afin_img = cv2.warpAffine(img,           # 入力画像
                                        afin_matrix,   # 行列
                                        (width,height)  # 解像度
                                        )

                cv2.imwrite(f"./edited_slide/slided_x_300_y_300_image/{x}_{y}{file}",afin_img)
                cv2.imwrite(f"./all_edited_file/{x}_{y}{file}",afin_img)
    #x=300y=300までを出力する処理

    for file in files:

        #画像読込
        img = cv2.imread(f"./images/{file}")

        # 画像サイズ
        height = img.shape[0]  # 高さ
        width  = img.shape[1]  # 幅

        #画像をpxずつ並行移動0,0が真ん中yは-で上に行く
        for x in range(0,-301,-20):
            for y in range(0,-301,-20):


                # 平行移動の変換行列を作成
                afin_matrix = np.float32([[1,0,x],[0,1,y]])

                # アファイン変換適用
                afin_img = cv2.warpAffine(img,           # 入力画像
                                        afin_matrix,   # 行列
                                        (width,height)  # 解像度
                                        )

                cv2.imwrite(f"./edited_slide/slided_x_-300_y_-300_image/{x}_{y}{file}",afin_img)
                cv2.imwrite(f"./all_edited_file/{x}_{y}{file}",afin_img)



