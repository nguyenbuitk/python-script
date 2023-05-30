from tkinter import *
root =Tk()

def printname(event):
	print("hello how are u")
# button-1 : chuột trái,-3 chuột phải

button_1=Button(root,text="print")
button_1.bind("<Button-1>",printname)
button_1.pack()

root.mainloop()