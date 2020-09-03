import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("wookdol GUI") # 창에 뜨는 타이틀
root.geometry("640x480")

progressbar1 = ttk.Progressbar(root,maximum=100, mode="indeterminate")
progressbar1.start(10) # 10ms마다 움직임
progressbar1.pack()

progressbar2 = ttk.Progressbar(root,maximum=100, mode="determinate")
progressbar2.start(10) # 10ms마다 움직임
progressbar2.pack()

p_var = DoubleVar() # 1.5%등의 실수단위이기 때문에 double
progressbar3 = ttk.Progressbar(root,maximum=100, length=150, variable=p_var)
progressbar3.pack()

def btncmd1():
    progressbar1.stop()
    progressbar2.stop()

def btncmd2():
    for i in range(101):
        time.sleep(0.01) # 0.01초 대기

        p_var.set(i) # progressbar의 값 설정
        progressbar3.update() # ui update를 통해 보기편하게
        print(p_var.get())
    

btn1 = Button(root, text="중지", command=btncmd1)
btn1.pack()

btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop()