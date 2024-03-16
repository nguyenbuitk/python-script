import tkinter as tk
from tkinter import* 
def manhinh1():
	root = tk.Tk()
	root.title("window")
	Button(root,text="play game").pack()
	root.geometry("350x350")
	root.mainloop()
class windowclass():
    def __init__(self, master,tk):
        self.master = master
        self.btn = tk.Button(master, text="Button", command=self.command)
        self.btn.pack()

    def command(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x350")
        Demo2(toplevel)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25)
        self.quitButton.pack()
        self.frame.pack()

manhinh1()