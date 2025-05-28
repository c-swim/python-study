from tkinter import *
from tkinter import messagebox

#함수
def keyEvent(event):
    if (event.keycode == 37) : # left : 37    
        messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 왼쪽 화살표")
    elif (event.keycode == 38) : # up : 38    
        messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 위쪽 화살표")
    elif (event.keycode == 39) : # right : 39    
        messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 오른쪽 화살표")
    elif (event.keycode == 40) : # down : 40    
        messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 아래쪽 화살표")
    
    
#메인
window = Tk()
window.bind("<Shift-Up>", keyEvent)
window.bind("<Shift-Down>", keyEvent)
window.bind("<Shift-Left>", keyEvent)
window.bind("<Shift-Right>", keyEvent)
window.mainloop()
