import glob
import os
import cv2
class Rota:

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


    files=[os.path.basename(f) for f in glob.glob(imagePath,recursive=True)
    if os.path.isfile(f)]#imagesフォルダのファイル名のみを取り出す



    dir="./edited_rota"
    countdir=(sum(os.path.isdir(os.path.join(dir, name)) for name in os.listdir(dir)))
    #edited_rotaのフォルダの数

    #写真を入れるためのフォルダを作る
    while True:
        if countdir<23:
            for i in range(45,331,45):
                os.makedirs("./edited_rota/rotated_{}_image".format(i),exist_ok=True)
                countdir-=1
            break
        else:
            pass

    #imageフォルダ内の写真を全て45°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-45
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_45_image/45-{}-{}".format(number,file),img_rotate)#45°に変えた画像をrotated_45_imagesに保存
        cv2.imwrite("./all_edited_file/r45-{}-{}".format(number,file),img_rotate)


    #imageフォルダ内の写真を全て90°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        img_rotate=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite("./edited_rota/rotated_90_image/90-{}-{}".format(number,file),img_rotate)#90°に変えた画像をrotated_90_imagesに保存
        cv2.imwrite("./all_edited_file/r90-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て135°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-135
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_135_image/135-{}-{}".format(number,file),img_rotate)#135°に変えた画像をrotated_135_imagesに保存
        cv2.imwrite("./all_edited_file/r135-{}-{}".format(number,file),img_rotate)


    #imageフォルダ内の写真を全て180°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))
        img_rotate=cv2.rotate(img,cv2.ROTATE_180)
        cv2.imwrite("./edited_rota/rotated_180_image/180-{}-{}".format(number,file),img_rotate)#180°に変えた画像をrotated_180_imagesに保存
        cv2.imwrite("./all_edited_file/r180-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て225°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-225
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_225_image/225-{}-{}".format(number,file),img_rotate)#225°に変えた画像をrotated_225_imagesに保存
        cv2.imwrite("./all_edited_file/r255-{}-{}".format(number,file),img_rotate)

  
    #imageフォルダ内の写真を全て270°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))
        img_rotate=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite("./edited_rota/rotated_270_image/270-{}-{}".format(number,file),img_rotate)#270°に変えた画像をrotated_270_imagesに保存
        cv2.imwrite("./all_edited_file/r270-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て315°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-315
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_315_image/315-{}-{}".format(number,file),img_rotate)#315°に変えた画像をrotated_315_imagesに保存
        cv2.imwrite("./all_edited_file/r315-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全てそのまま保存
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=0
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./all_edited_file/r0-{}-{}".format(number,file),img_rotate)










