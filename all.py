from rota import rota
from slide import slide

ques=input("rotation実行しますか？(y/n)→")
ques2=input("slide実行しますか？(y/n)→")

if "y" in ques:
    print("rotation実行します")
    rota()
else:
    print("飛ばします")
    pass

if "y" in ques2:
    print("slide実行します")
    slide()
else:
    print("飛ばします")
    pass