def All():
    import os

    os.makedirs("./all_edited_file",exist_ok=True)
    os.makedirs("./edited_rota",exist_ok=True)
    os.makedirs("./edited_slide",exist_ok=True)
    os.makedirs("./edited_rotaxslide",exist_ok=True)


    from rota import Rota
    from slide import Slide
    from rotaxslide import RotaxSlide

    RotaxSlide()
    print("rotaxslide実行しました")

    Slide()
    print("slide実行しました")

    Rota()
    print("rota実行しました")

   
    
    
    


    
All()
    