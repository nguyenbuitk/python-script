from tkinter import *

class nhaptien():
	def __init__(self,master):
		self.master=master
		Label(master, text="tien nap").grid(row=0)
		Label(master, text="tien cuoc").grid(row=1)
		self.e1= Entry(master)
		self.e2 = Entry(master)
		self.e1.grid(row=0, column=1)
		self.e2.grid(row=1, column=1)
		Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
		Button(master, text='Show', command=self.show).grid(row=3, column=1, sticky=W, pady=4)
	def show(self):
		global a
		a=int(self.e1.get())

master=Tk()
tien=nhaptien(master)
mainloop()
tn=4
if type(a)==type(tn):
	print("tesdf")
