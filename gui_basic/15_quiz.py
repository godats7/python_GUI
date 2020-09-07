# quiz) tkinter를 이용한 메모장 프로그램 만들기

# GUI조건
# 1. title : 제목 없음 - Windows 메모장
# 2. 메뉴 :  파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 :  파일 메뉴내에서 열기, 저장, 끝내기, 3개만 처리
# 4. 프로그램 시작시 본문은 비어있는 상태
import os
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("제목없음 - Windows 메모장") # 창에 뜨는 타이틀
root.geometry("640x480")

filename="mynote.txt"

def create_new_file():
    print("새 파일을 만듭니다")

def open_file():
    if os.path.isfile(filename): # 파일이 있으면True 아니면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())            
    print("파일을 엽니다")

def save_file():
    if os.path.isfile(filename):              
        response = msgbox.askyesno(message="동일한 파일명이 존재합니다. 덮어씌우시겠습니까?")
        if response == 1:
            with open(filename, "w", encoding="utf8") as file:
                file.write(txt.get("1.0",END))
                print("파일을 덮어씌웁니다.")            
        elif response == 0:
            print("파일을 저장하지 않습니다.")
    else:
        with open(filename, "w", encoding="utf8") as file:
                file.write(txt.get("1.0",END))
                print("파일을 저장합니다.") 
    

menu = Menu(root)

# 파일
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Create New File",command = create_new_file)
menu_file.add_command(label="Open File",command = open_file)
menu_file.add_command(label="Save File",command = save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

# 편집
menu.add_cascade(label="Edit")

# 서식
menu.add_cascade(label="Option")

# 보기
menu.add_cascade(label="View")

# 도움말
menu.add_cascade(label="Help")

# 스크롤바
scrollbar =  Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 텍스트 입력공간
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True) # fill은 영역 전체 채우기


scrollbar.config(command=txt.yview)

root.config(menu=menu)

root.mainloop()