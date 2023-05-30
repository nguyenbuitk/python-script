import tkinter as tk
from tkinter import*
from tkinter import *

class manhinh1():
	def __init__(self,master):
		screen1=Tk()
		screen1.geometry("500x500")
		screen1.title("Race Turtle")
		Label(text="").pack()
		Label(text="").pack()
		Label(text="").pack()
		Label(text="RACE TURTLE",width="300",height="2",font=("calibri",13)).pack()
		Label(text="").pack()
		Label(text="").pack()
		Button(text="Login",height=2,width=30,command=login_2).pack()
		Label(text="").pack()
		Label(text="").pack()
		Button(text="Register",height=2,width=30,command=register_2).pack()
		screen1.mainloop()
	def command(self):
		self.master.withdraw()
		toplevel=Toplevel(self.master)
		toplevel.geometry("350x350")
		Demo2(toplevel)

class Demo2:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.quitButton = tk.Button(self.frame, text = 'Quit', height=2, command = self.close_windows)
		self.quitButton.pack()
		self.frame.pack()
	def close_windows(self):
		self.master.destroy()

root=Tk()
root.geometry("350x350")
cls=manhinh1(root)
root.mainloop()