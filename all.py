from rota import rota
from slide import slide
from flip import flip

ques_r=input("rotation実行しますか？(y/n)→")
ques_s=input("slide実行しますか？(y/n)→")
ques_f=input("flip実行しますか(y/n)→")

if "y" in ques_r:
    print("rotation実行します")
    rota()

else:
    print("飛ばします")
    pass

if "y" in ques_s:
    print("slide実行します")
    slide()
else:
    print("飛ばします")
    pass

if "y" in ques_f:
    print("flip実行します")
    flip()
else:
    print("飛ばします")
    pass