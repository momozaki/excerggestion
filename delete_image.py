import shutil
import os

path='./edited'
move_to="./ゴミ箱"

list_dir_name=os.listdir(path)

#editedフォルダの中身をゴミ箱に移動させる
for i in list_dir_name:
    join_path=os.path.join(path,i)
    move_path=os.path.join(move_to,i)

    if os.path.isdir(join_path):
        shutil.move(join_path,move_path)



ans=input("ついでにゴミ箱の中身も全部消す？(yes/no)→")
file_exists=os.path.isfile("./ゴミ箱")
if "y" in ans:

    shutil.rmtree("./ゴミ箱/")
    os.mkdir("ゴミ箱")
    print("ゴミ箱の中を全削除しました")


else:
    print("削除しませんでした。")
    pass





