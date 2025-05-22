from tkinter import *
from tkinter import messagebox

#함수
def keyEvent(event):
    if (event.keycode == 38) : # up : 38    
        messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + " + chr(38))
    
#메인
window = Tk()
window.bind("<Shift-Up>", keyEvent)
window.bind("<Shift-Down>", keyEvent)
window.bind("<Shift-Left>", keyEvent)
window.bind("<Shift-Right>", keyEvent)
window.mainloop()
