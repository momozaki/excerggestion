import glob
import os
import cv2
class rota:

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
        if countdir<20:
            for i in range(15,331,15):
                os.makedirs("./edited_rota/rotated_{}_image".format(i),exist_ok=True)
                countdir-=1
            break

    #imageフォルダ内の写真を全て15°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-15
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_15_image/15-{}-{}".format(number,file),img_rotate)#15°に変えた画像をrotated_15_imagesに保存
        cv2.imwrite("./all_edited_file/r15-{}-{}".format(number,file),img_rotate)
    #imageフォルダ内の写真を全て30°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-30
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_30_image/30-{}-{}".format(number,file),img_rotate)#30°に変えた画像をrotated_30_imagesに保存
        cv2.imwrite("./all_edited_file/r30-{}-{}".format(number,file),img_rotate)

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

    #imageフォルダ内の写真を全て60°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-60
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_60_image/60-{}-{}".format(number,file),img_rotate)#60°に変えた画像をrotated_60_imagesに保
        cv2.imwrite("./all_edited_file/r60-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て75°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-75
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_75_image/75-{}-{}".format(number,file),img_rotate)#75°に変えた画像をrotated_75_imagesに保存
        cv2.imwrite("./all_edited_file/r75-{}-{}".format(number,file),img_rotate)


    #imageフォルダ内の写真を全て90°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        img_rotate=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite("./edited_rota/rotated_90_image/90-{}-{}".format(number,file),img_rotate)#90°に変えた画像をrotated_90_imagesに保存
        cv2.imwrite("./all_edited_file/r90-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て105°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-105
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_105_image/105-{}-{}".format(number,file),img_rotate)#105°に変えた画像をrotated_105_imagesに保存
        cv2.imwrite("./all_edited_file/r105-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て120°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-120
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_120_image/120-{}-{}".format(number,file),img_rotate)#120°に変えた画像をrotated_120_imagesに保存
        cv2.imwrite("./all_edited_file/r120-{}-{}".format(number,file),img_rotate)

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

    #imageフォルダ内の写真を全て150°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-150
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_150_image/150-{}-{}".format(number,file),img_rotate)#150°に変えた画像をrotated_150_imagesに保存
        cv2.imwrite("./all_edited_file/r150-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て165°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-165
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_165_image/165-{}-{}".format(number,file),img_rotate)#165°に変えた画像をrotated_165_imagesに保存
        cv2.imwrite("./all_edited_file/r165-{}-{}".format(number,file),img_rotate)


    #imageフォルダ内の写真を全て180°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))
        img_rotate=cv2.rotate(img,cv2.ROTATE_180)
        cv2.imwrite("./edited_rota/rotated_180_image/180-{}-{}".format(number,file),img_rotate)#180°に変えた画像をrotated_180_imagesに保存
        cv2.imwrite("./all_edited_file/r180-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て195°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-195
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_195_image/195-{}-{}".format(number,file),img_rotate)#195°に変えた画像をrotated_195_imagesに保存
        cv2.imwrite("./all_edited_file/r195-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て210°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-210
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_210_image/210-{}-{}".format(number,file),img_rotate)#210°に変えた画像をrotated_210_imagesに保存
        cv2.imwrite("./all_edited_file/r210-{}-{}".format(number,file),img_rotate)

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

    #imageフォルダ内の写真を全240°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-240
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_240_image/240-{}-{}".format(number,file),img_rotate)#240°に変えた画像をrotated_240_imagesに保存
        cv2.imwrite("./all_edited_file/r240-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て255°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-255
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_255_image/255-{}-{}".format(number,file),img_rotate)#255°に変えた画像をrotated_255_imagesに保存
        cv2.imwrite("./all_edited_file/r255-{}-{}".format(number,file),img_rotate)


    #imageフォルダ内の写真を全て270°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))
        img_rotate=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite("./edited_rota/rotated_270_image/270-{}-{}".format(number,file),img_rotate)#270°に変えた画像をrotated_270_imagesに保存
        cv2.imwrite("./all_edited_file/r270-{}-{}".format(number,file),img_rotate)

        #imageフォルダ内の写真を全て285°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-285
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_285_image/285-{}-{}".format(number,file),img_rotate)#285°に変えた画像をrotated_285_imagesに保存
        cv2.imwrite("./all_edited_file/r285-{}-{}".format(number,file),img_rotate)

    #imageフォルダ内の写真を全て300°傾ける処理
    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-300
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rota/rotated_300_image/300-{}-{}".format(number,file),img_rotate)#300°に変えた画像をrotated_300_imagesに保存
        cv2.imwrite("./all_edited_file/r300-{}-{}".format(number,file),img_rotate)

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


    for number,file in enumerate(files):
        img=cv2.imread("./images/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=0
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))#0°
        cv2.imwrite("./all_edited_file/r0-{}-{}".format(number,file),img_rotate)










