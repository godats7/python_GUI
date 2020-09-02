from tkinter import *

root = Tk()
root.title("wookdol GUI") # 창에 뜨는 타이틀
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0) # height값이 0일때는 전체를 보여주지만 1일때는 첫번째만, 2일때는 2번째까지만 보여준다
listbox.insert(0,"apple")
listbox.insert(1,"strawberry")
listbox.insert(2,"banana")
listbox.insert(END,"watermelon")
listbox.insert(END,"grape")
listbox.pack()

def btncmd():

    # 삭제
    # listbox.delete(END) # 맨 뒤의 항목을 삭제
    # listbox.delete(0) # 맨 위의 항목을 삭제

    # 갯수 확인
    print("리스트에는 ",listbox.size(),"개가 있어요")

    # 시작과 끝인덱스로 범위지정
    print("1번부터 3번까지의 항목",listbox.get(0,2))

    # 선택된 항목 확인(위치로 반환)(드래그 혹은 클릭이나 ctrl+클릭으로 항목 선택)
    print("선택된 항목 : ",listbox.curselection())
    

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()