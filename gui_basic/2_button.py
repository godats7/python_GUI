from tkinter import *

root = Tk()
root.title("wookdol GUI") # 창에 뜨는 타이틀

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼222222222") # 버튼 내에서 글자를 기준으로 x축과 y축의 간격을 넣는다
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 버튼의 고정크기
btn4.pack()

btn5 = Button(root, width=10, height=3, text="버튼4444444444444")
btn5.pack()

bgcolor="#40E0D0"

btn6 = Button(root, fg="red", bg=bgcolor, text="버튼5") # fg는 글자색, bg는 버튼 배경색
btn6.pack()

photo = PhotoImage(file="gui_basic/image.png")

btn7 = Button(root, image=photo)
btn7.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn8 = Button(root, text="동작하는 버튼", command=btncmd)
btn8.pack()

root.mainloop()