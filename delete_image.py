import shutil
import os

rota_path='./edited_rota'
slide_path="./edited_slide"
rotaxslide_path="./edited_rotaxslide"


move_to="./ゴミ箱"

list_rota_dir_name=os.listdir(rota_path)
list_slide_dir_name=os.listdir(slide_path)
list_rotaxslide_dir_name=os.listdir(rotaxslide_path)



#edited_rotaフォルダの中身をゴミ箱に移動させる
for i in list_rota_dir_name:
    join_path=os.path.join(rota_path,i)
    move_path=os.path.join(move_to,i)

    if os.path.isdir(join_path):
        shutil.move(join_path,move_path)


#edited_slideフォルダの中身をゴミ箱に移動させる
for i in list_slide_dir_name:
    join_path=os.path.join(slide_path,i)
    move_path=os.path.join(move_to,i)

    if os.path.isdir(join_path):
        shutil.move(join_path,move_path)

#edited_rotaxslideフォルダの中身をゴミ箱に移動させる
for i in list_rotaxslide_dir_name:
    join_path=os.path.join(rotaxslide_path,i)
    move_path=os.path.join(move_to,i)

    if os.path.isdir(join_path):
        shutil.move(join_path,move_path)






ans=input("all_edited_fileの中身も全部けす？(yes/no)→")

if "y" in ans:

    shutil.rmtree("./all_edited_file/")
    os.mkdir("all_edited_file")
    print("all_edited_fileの中を全削除しました")


else:
    print("削除しませんでした。")
    pass


ans2=input("ついでにゴミ箱の中身も全部消す？(yes/no)→")
file_exists=os.path.isfile("./ゴミ箱")
if "y" in ans2:

    shutil.rmtree("./ゴミ箱/")
    os.mkdir("ゴミ箱")
    print("ゴミ箱の中を全削除しました")


else:
    print("削除しませんでした。")
    pass





