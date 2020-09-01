from tkinter import *

root = Tk()
root.title("wookdol GUI") # 창에 뜨는 타이틀
# root.geometry("640x480") # 창의 사이즈 가로*세로
root.geometry("640x480+500+300") # 가로 * 세로 + x축좌표 + y축 좌표

root.resizable(False,False) # 너비x, 높이y 값 변경 불가

root.mainloop()