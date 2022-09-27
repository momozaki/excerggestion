import glob
import os
import cv2
class RotaxSlide:

    slidePath="./edited_slide/slided_x_300_y_300_image/*"
    minus_slidePath="./edited_slide/slided_x_-300_y_-300_image/*"

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


    slided_files=[os.path.basename(f) for f in glob.glob(slidePath,recursive=True)
    if os.path.isfile(f)]#slided_x_300_y_300_imageフォルダのファイル名のみを取り出す

    minus_slided_files=[os.path.basename(f) for f in glob.glob(minus_slidePath,recursive=True)
    if os.path.isfile(f)]#slided_x_-300_y_-300_imageフォルダのファイル名のみを取り出す



    dir="./edited_rotaxslide"
    countdir=(sum(os.path.isdir(os.path.join(dir, name)) for name in os.listdir(dir)))
    #edited_rotaxslideのフォルダの数

    #写真を入れるためのフォルダを作る
    while True:
        if countdir<23:
            for i in range(45,331,45):
                os.makedirs("./edited_rotaxslide/rotaxslide_{}_image".format(i),exist_ok=True)
                countdir-=1
            break
        else:
            pass

    while True:
        if countdir<23:
            for i in range(45,331,45):
                os.makedirs("./edited_rotaxslide/minus_rotaxslide_{}_image".format(i),exist_ok=True)
                countdir-=1
            break
        else:
            pass

    
    #slided_filesフォルダ内の写真を全て45°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_300_y_300_image/{0}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-45
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rotaxslide/rotaxslide_45_image/rs45-{}-{}".format(number,file),img_rotate)#45°に変えた画像をrotaxslide_45_imagesに保存
        cv2.imwrite("./all_edited_file/rs45-{}-{}".format(number,file),img_rotate)


    #slided_filesフォルダ内の写真を全て90°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_300_y_300_image/{}".format(file))#絶対パスのみ
        img_rotate=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite("./edited_rotaxslide/rotaxslide_90_image/rs90-{}-{}".format(number,file),img_rotate)#90°に変えた画像をrotaxslide_90_imagesに保存
        cv2.imwrite("./all_edited_file/rs90-{}-{}".format(number,file),img_rotate)

    #slided_filesフォルダ内の写真を全て135°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_300_y_300_image/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-135
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rotaxslide/rotaxslide_135_image/rs135-{}-{}".format(number,file),img_rotate)#135°に変えた画像をrotaxslide_135_imagesに保存
        cv2.imwrite("./all_edited_file/rs135-{}-{}".format(number,file),img_rotate)


    #slided_filesフォルダ内の写真を全て180°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_300_y_300_image/{}".format(file))
        img_rotate=cv2.rotate(img,cv2.ROTATE_180)
        cv2.imwrite("./edited_rotaxslide/rotaxslide_180_image/rs180-{}-{}".format(number,file),img_rotate)#180°に変えた画像をrotaxslide_180_imagesに保存
        cv2.imwrite("./all_edited_file/rs180-{}-{}".format(number,file),img_rotate)

    #slided_filesフォルダ内の写真を全て225°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_300_y_300_image/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-225
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rotaxslide/rotaxslide_225_image/rs225-{}-{}".format(number,file),img_rotate)#225°に変えた画像をrotaxslide_225_imagesに保存
        cv2.imwrite("./all_edited_file/rs255-{}-{}".format(number,file),img_rotate)

  
    #slided_filesフォルダ内の写真を全て270°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_300_y_300_image/{}".format(file))
        img_rotate=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite("./edited_rotaxslide/rotaxslide_270_image/rs270-{}-{}".format(number,file),img_rotate)#270°に変えた画像をrotaxslide_270_imagesに保存
        cv2.imwrite("./all_edited_file/rs270-{}-{}".format(number,file),img_rotate)

    #slided_filesフォルダ内の写真を全て315°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_300_y_300_image/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-315
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rotaxslide/rotaxslide_315_image/rs315-{}-{}".format(number,file),img_rotate)#315°に変えた画像をrotaxslide_315_imagesに保存
        cv2.imwrite("./all_edited_file/rs315-{}-{}".format(number,file),img_rotate)


    #minus_slided_filesフォルダ内の写真を全て45°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_-300_y_-300_image/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-45
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rotaxslide/rotaxslide_45_image/rs45-{}-{}".format(number,file),img_rotate)#45°に変えた画像をrotaxslide_45_imagesに保存
        cv2.imwrite("./all_edited_file/rs45-{}-{}".format(number,file),img_rotate)


    #minus_slided_filesフォルダ内の写真を全て90°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_-300_y_-300_image/{}".format(file))#絶対パスのみ
        img_rotate=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite("./edited_rotaxslide/rotaxslide_90_image/rs90-{}-{}".format(number,file),img_rotate)#90°に変えた画像をrotaxslide_90_imagesに保存
        cv2.imwrite("./all_edited_file/rs90-{}-{}".format(number,file),img_rotate)

    #minus_slided_filesフォルダ内の写真を全て135°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_-300_y_-300_image/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-135
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rotaxslide/rotaxslide_135_image/rs135-{}-{}".format(number,file),img_rotate)#135°に変えた画像をrotaxslide_135_imagesに保存
        cv2.imwrite("./all_edited_file/rs135-{}-{}".format(number,file),img_rotate)


    #minus_slided_filesフォルダ内の写真を全て180°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_-300_y_-300_image/{}".format(file))
        img_rotate=cv2.rotate(img,cv2.ROTATE_180)
        cv2.imwrite("./edited_rotaxslide/rotaxslide_180_image/rs180-{}-{}".format(number,file),img_rotate)#180°に変えた画像をrotaxslide_180_imagesに保存
        cv2.imwrite("./all_edited_file/rs180-{}-{}".format(number,file),img_rotate)

    #minus_slided_filesフォルダ内の写真を全て225°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_-300_y_-300_image/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-225
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rotaxslide/rotaxslide_225_image/rs225-{}-{}".format(number,file),img_rotate)#225°に変えた画像をrotaxslide_225_imagesに保存
        cv2.imwrite("./all_edited_file/rs255-{}-{}".format(number,file),img_rotate)

  
    #minus_slided_filesフォルダ内の写真を全て270°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_-300_y_-300_image/{}".format(file))
        img_rotate=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite("./edited_rotaxslide/rotaxslide_270_image/rs270-{}-{}".format(number,file),img_rotate)#270°に変えた画像をrotaxslide_270_imagesに保存
        cv2.imwrite("./all_edited_file/rs270-{}-{}".format(number,file),img_rotate)

    #minus_slided_filesフォルダ内の写真を全て315°傾ける処理
    for number,file in enumerate(slided_files):
        img=cv2.imread("./slided_x_-300_y_-300_image/{}".format(file))#絶対パスのみ
        (h,w)=img.shape[:2]
        center=(w/2,h/2)
        angle=-315
        scale=1
        M=cv2.getRotationMatrix2D(center,angle,scale)
        img_rotate=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite("./edited_rotaxslide/rotaxslide_315_image/rs315-{}-{}".format(number,file),img_rotate)#315°に変えた画像をrotaxslide_315_imagesに保存
        cv2.imwrite("./all_edited_file/rs315-{}-{}".format(number,file),img_rotate)