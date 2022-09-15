import shutil
import os

dir = './edited'

countdir=(sum(os.path.isdir(os.path.join(dir, name)) for name in os.listdir(dir)))
#editedのフォルダの数

path=dir
move_to="./ゴミ箱"

list_dir_name=os.listdir(path)

#editedフォルダの中身をゴミ箱に移動させる
for i in list_dir_name:
    join_path=os.path.join(path,i)
    move_path=os.path.join(move_to,i)

    if os.path.isdir(join_path):
        shutil.move(join_path,move_path)


"""
ans=str(input("ついでにゴミ箱の中身も全部消す？(yes/no)"))

if ans=="yes" or "YES" or "イエス" or "いえす":

    shutil.rmtree("./ゴミ箱")
    os.mkdir("ゴミ箱")

elif ans=="no":
    pass
"""


