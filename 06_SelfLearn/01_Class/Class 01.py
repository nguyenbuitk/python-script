from tkinter import *

class sieunhan:
	def __init__(self,master,para_ten,para_vukhi,para_mausac):
		self.master=master
		self.ten=" sieu nhan "+para_ten
		self.vukhi=para_vukhi
		self.para_mausac=para_mausac
		self.e="3"
		self.f="4"
		Button(master,text="show",command=self.xinchao).pack()
	def xinchao(self):
		return int(self.e)+int(self.f)
master=Tk()
sieunhana=sieunhan(master,"kteam","dsafa","sdfa")


