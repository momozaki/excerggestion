import glob
import os
import cv2
import numpy as np


befores=[os.path.basename(f) for f in glob.glob("./images/*",recursive=True)
if os.path.isfile(f)]#imagesフォルダのファイルを取り出す

#日本語のファイルを開くためまずnumpyで画像ファイルを開く
for before in befores:
    buf=np.fromfile(before,np.uint8)
    beforefile=cv2.imdecode(buf,cv2.IMREAD_UNCHANGED)
    
    for file in beforefile:
        img=cv2.imread(file)
        img_rotate=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("test",img_rotate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cv2.imwrite("./rotated_image/.jpg",img_rotate)




