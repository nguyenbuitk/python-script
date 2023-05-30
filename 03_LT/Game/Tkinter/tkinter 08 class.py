from tkinter import *
class nutnhan:	

	def __init__(self,master):
		frame=Frame(master)
		frame.pack()
		self.printbutton=Button(frame,text="print",command=self.printmassage)
		self.printbutton.pack()

		self.quitbutton=Button(frame,text="quit",command=frame.quit)
		self.quitbutton.pack()

	def printmassage(self):
		print("fuck you")	


root=Tk()
b=nutnhan(root);
root.mainloop();