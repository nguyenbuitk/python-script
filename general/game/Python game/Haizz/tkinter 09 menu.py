from tkinter import*

def donothing():
	print("ok ok i won't")

root=Tk()

menu=Menu(root)
root.config(menu=menu)
submenu2=Menu(menu)
submenu1=Menu(menu)
menu.add_cascade(label="file",menu=submenu1)
submenu1.add_command(label="now...",command=donothing)
# dấu gạch ngang

submenu1.add_separator()
submenu1.add_command(label="play again",command=donothing)
menu.add_cascade(label="edit",menu=submenu2)
submenu2.add_command(label="print",command=donothing)
root.mainloop()