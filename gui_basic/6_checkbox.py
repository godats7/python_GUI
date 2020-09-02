from tkinter import *

root = Tk()
root.title("wookdol GUI") # 창에 뜨는 타이틀
root.geometry("640x480")

chkvar = IntVar() # chkvar에 int형으로 값을 저장한다.
chkbox = Checkbutton(root,text="오늘 하루 보지않기", variable=chkvar)
# chkbox.select() # 자동으로 선택처리
# chkbox.deselect() # 자동으로 선택해제처리(기본)
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0은 체크해제 1은 체크상태
    print(chkvar2.get())
    

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()