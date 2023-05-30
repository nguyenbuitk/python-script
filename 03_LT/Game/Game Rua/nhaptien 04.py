from tkinter import *

def nhaptien():
	global a
	Label(master, text="tien nap").grid(row=0)
	Label(master, text="tien cuoc").grid(row=1)
	e1= Entry(master)
	e2 = Entry(master)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
	Button(master, text='Show').grid(row=3, column=1, sticky=W, pady=4)
def show():
	

master=Tk()
nhaptien()
mainloop()
print(a)