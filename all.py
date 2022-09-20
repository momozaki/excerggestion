import os

os.makedirs("./all_edited_file",exist_ok=True)
os.makedirs("./edited_rota",exist_ok=True)
os.makedirs("./edited_slide",exist_ok=True)
os.makedirs("./edited_flip",exist_ok=True)


from rota import Rota
from slide import Slide
from flip import Flip


Rota()
print("rota実行しました")

Slide()
print("slide実行しました")

Flip()
print("flip実行しました")
   