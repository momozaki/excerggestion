import cv2
import glob
import os
class flip:

    imagePath="./images/*"
    dir="./edited_flip"
    countdir=(sum(os.path.isdir(os.path.join(dir, name)) for name in os.listdir(dir)))
            #edited_flipのフォルダの数


    #写真を入れるためのフォルダを作る
    if countdir<2:
        os.makedirs("./edited_flip/fliped_lr_image",exist_ok=True)
        os.makedirs("./edited_flip/fliped_udlr_image",exist_ok=True)

    files=[os.path.basename(f) for f in glob.glob(imagePath,recursive=True)
        if os.path.isfile(f)]#imagesフォルダのファイル名のみを取り出す

    for file in files:#画像を左右反転してedited_flipフォルダに入れる処理
        img=cv2.imread(f"./images/{file}")
        img_flip_lr=cv2.flip(img,1)
        cv2.imwrite(f"./edited_flip/fliped_lr_image/fliped_lr_{file}",img_flip_lr)
        cv2.imwrite(f"./all_edited_file/fliped_lr_{file}",img_flip_lr)

    for file in files:#画像を上下左右反転してedited_flipフォルダに入れる処理
        img=cv2.imread(f"./images/{file}")
        img_flip_udlr=cv2.flip(img,-1)
        cv2.imwrite(f"./edited_flip/fliped_udlr_image/fliped_udlr_{file}",img_flip_udlr)
        cv2.imwrite(f"./all_edited_file/fliped_udlr_{file}",img_flip_lr)

