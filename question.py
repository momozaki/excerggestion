import tkinter as tk
frm=tk.Tk()
frm.geometry("800x800")
frm.title("test")

buttonA=tk.Button(frm, text="AAA").pack(side=tk.LEFT)
buttonB=tk.Button(frm, text="BBB").pack(side=tk.RIGHT)

tk.mainloop()