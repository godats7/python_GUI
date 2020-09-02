from tkinter import *

root = Tk()
root.title("wookdol GUI") # 창에 뜨는 타이틀
root.geometry("640x480")

txt  =Text(root, width=30, height=5)
txt.pack()

txt.insert(END,"글자를 입력하세요")

e =Entry(root,width=30) # 로그인 아이디 등의 한줄입력(enter가 안됨)
e.pack()
e.insert(0,"한줄만 입력하세요")

def btncmd():
    # 내용 입력
    print(txt.get("1.0",END)) # 1번째 줄의 0번컬럼(맨 처음부터 가져온다)
    print(e.get())

    # 내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()