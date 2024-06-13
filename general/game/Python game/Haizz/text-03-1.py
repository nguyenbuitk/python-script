import tkinter as tk
import turtle
from random import randint
from tkinter import *
global username
global password
global tiencuoc
class windowclass():
	def __init__(self, master):
		self.master = master
		Label(self.master,text="").pack()
		Label(self.master,text="").pack()
		Label(self.master,text="").pack()
		Label(self.master,text="").pack()
		Label(self.master,text="RACE TURTLE",width="300",height="2",font=("calibri",13)).pack()
		Label(self.master,text="").pack()
		Label(self.master,text="").pack()
		Button(master,text="Login",height=2,width=30,command=self.command1).pack()
		Label(master,text="").pack()
		Label(master,text="").pack()
		Button(master,text="Register",height=2,width=30,command=self.command2).pack()
	def command1(self):
		self.master.withdraw()
		toplevel = Toplevel(self.master)
		toplevel.geometry("350x350")
		login_2(toplevel)
	def command2(self):
		self.master.withdraw()
		toplevel = Toplevel(self.master)
		toplevel.geometry("350x350")
		register_2(toplevel)
class login_2:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		Label(master,text="").pack()
		Label(master,text="").pack()
		Label(master,text="").pack()
		self.button1=tk.Button(master,text="Play Game",height=2,width=30,command=self.command2_1).pack()
		Button(master,text="Help",height=2,width=30).pack()
		Button(master,text="Height Score",height=2,width=30).pack()
		Button(master,text="Exit",height=2,width=30,command=quit).pack()
	def command2_1(self):
		self.master.withdraw()
		toplevel=Toplevel(self.master)
		toplevel.geometry("350x350")
		nhaptien(toplevel)
class nhaptien:
	def __init__(self,master):
		self.master=master
		self.frame=Frame(self.master)
		global tiennap
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
		playgame1()
		return self.tiencuoc
class register_2:
	def __init__(self,master):
		self.master=master
		self.frame = tk.Frame(self.master)
		global username_entry
		global password_entry
		username = StringVar()
		password = StringVar()
		Label(self.master, text = "Please enter details below").pack()
		Label(self.master, text = "").pack()
		Label(self.master,text = "Username * ").pack()
		username_entry = Entry(self.master,textvariable = username)
		username_entry.pack()
		Label(self.master, text = "Password * ").pack()
		password_entry =  Entry(self.master, textvariable = password)
		password_entry.pack()
		Label(self.master, text = "").pack()
		Button(self.master, text = "Register", width = 10, height = 1,command=self.playgame).pack()

	def playgame(self):
		self.master.withdraw()
		tina = turtle.Turtle()
		tina.speed(100)
		tina.penup()
		tina.goto(-140,140)
		for step in range(16):
			#tina.write(step,align='center');
			tina.right(90);
			tina.forward(10);
			tina.pendown();
			tina.forward(190);
			tina.penup();
			tina.backward(200);
			tina.left(90);
			tina.forward(20)
		red=turtle.Turtle()
		red.color("red")
		red.shape("turtle")
		red.penup()
		red.goto(-160,100)
		red.pendown()
		blue=turtle.Turtle()
		blue.color("blue")
		blue.shape("turtle")
		blue.penup()
		blue.goto(-160,60)
		blue.pendown()
		yellow=turtle.Turtle()
		yellow.color("yellow")
		yellow.shape("turtle")
		yellow.penup()
		yellow.goto(-160,20)
		yellow.pendown()
		black=turtle.Turtle()
		black.color("black")
		black.shape("turtle")

		black.penup()
		black.goto(-160,-20)
		black.pendown()

		for turn in range(100):
		   
		    red.forward(randint(1,5))
		    blue.forward(randint(1,5))
		    yellow.forward(randint(1,5))
		    black.forward(randint(1,5))

		wn=turtle.Screen()
		exit()
		game = Tk()
		self.master.withdraw()
		game.title("RESULT")
		screen = Canvas(game, width=500, height=400, background="pink")
		screen.pack()
		rect = screen.create_rectangle(25,25,475,375, fill="white", outline="blue")
		screen.update()
		text = screen.create_text(100,50,text ="Name:", fill="blue", font=("Arial", 15))
		text = screen.create_text(100,150,text ="Score:", fill="blue", font=("Arial", 15))
		btn_exit = Button(game, text='Back', font=("Arial", 14, "bold"),bg="cyan", fg="green", width=10, height=1, command=returnplay)
		btn_exit.pack()
		btn_exit.place(x=0,y=0)
		game.mainloop()
		
def playgame1():
	tina = turtle.Turtle()
	tina.speed(100)
	tina.penup()
	tina.goto(-140,140)
	for step in range(16):
		#tina.write(step,align='center');
		tina.right(90);
		tina.forward(10);
		tina.pendown();
		tina.forward(190);
		tina.penup();
		tina.backward(200);
		tina.left(90);
		tina.forward(20)
	red=turtle.Turtle()
	red.color("red")
	red.shape("turtle")

	red.penup()
	red.goto(-160,100)
	red.pendown()

	blue=turtle.Turtle()
	blue.color("blue")
	blue.shape("turtle")

	blue.penup()
	blue.goto(-160,60)
	blue.pendown()

	yellow=turtle.Turtle()
	yellow.color("yellow")
	yellow.shape("turtle")

	yellow.penup()
	yellow.goto(-160,20)
	yellow.pendown()

	black=turtle.Turtle()
	black.color("black")
	black.shape("turtle")

	black.penup()
	black.goto(-160,-20)
	black.pendown()

	for turn in range(100):

		red.forward(randint(1,5))
		blue.forward(randint(1,5))
		yellow.forward(randint(1,5))
		black.forward(randint(1,5))

	wn=turtle.Screen()
	game = Tk()
	game.title("RESULT")
	screen = Canvas(game, width=500, height=400, background="pink")
	screen.pack()
	rect = screen.create_rectangle(25,25,475,375, fill="white", outline="blue")
	screen.update()
	text = screen.create_text(100,50,text ="Name:", fill="blue", font=("Arial", 15))
	text = screen.create_text(100,150,text ="Score:", fill="blue", font=("Arial", 15))
	btn_exit = Button(game, text='Back', font=("Arial", 14, "bold"),bg="cyan", fg="green", width=10, height=1,command=returnplay)
	btn_exit.pack()
	btn_exit.place(x=0,y=0)
	game.mainloop()

def returnplay():
	root = Tk()
	root.title("window")
	root.geometry("350x350")
	windowclass(root)
	root.mainloop()
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
root = Tk()
root.title("window")
root.geometry("350x350")
windowclass(root)
root.mainloop()