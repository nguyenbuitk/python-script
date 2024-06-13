from tkinter import*

class nhaptien:
	def __init__(self,master):
		self.master=master
		self.frame=Frame(self.master)
		global tiennap
		global tiencuoc
		global tiennap_entry
		global tiencuoc_entry
		global chonrua
		global chonrua_entry
		tiennap=StringVar()
		tiencuoc=StringVar()
		chonrua=StringVar()
		Label(self.master,text="Please enter deposit money and bet money").pack()
		Label(self.master,text="").pack()
		Label(self.master,text="deposit money").pack()
		tiennap_entry=Entry(self.master,textvariable=tiennap)
		tiennap_entry.pack()
		Label(self.master,text="bet money").pack()
		tiencuoc_entry=Entry(self.master,textvariable=tiencuoc)
		tiencuoc_entry.pack()
		Label(self.master,text="").pack()
		Label(self.master,text="chose the turtle you want (1-4) ").pack()
		chonrua_entry=Entry(self.master,textvariable=chonrua)
		chonrua_entry.pack()
		Button(self.master,text="Play",width=10,height=1,command=self.command3_1).pack()
	def command3_1(self):
		self.master.withdraw()
		return tiencuoc.set()

root = Tk()
root.title("window")
root.geometry("350x350")
nhaptien1=nhaptien(root)
root.mainloop()
