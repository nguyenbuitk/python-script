from tkinter import *
import turtle
from random import randint
global screen1
global screen2_1
global game

def manhinh1():
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
	exit()
def login_2():
	screen2_1=Tk()
	screen2_1.geometry("500x500")
	screen2_1.title("Menu")
	Label(screen2_1,text="").pack()
	Label(screen2_1,text="").pack()
	Label(screen2_1,text="").pack()
	Label(screen2_1,text="").pack()
	Button(screen2_1,text="Play Game",height=2,width=30,command=nhaptien_3).pack()
	Button(screen2_1,text="Help",height=2,width=30).pack()
	Button(screen2_1,text="Height Score",height=2,width=30).pack()
	Button(screen2_1,text="Exit",height=2,width=30,command=quit).pack()
	screen2_1.mainloop()
def register_2():
  global screen2_2
  screen2_2=Tk()

  screen2_2.title("Register")
  screen2_2.geometry("300x250")
   
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
 
  Label(screen2_2, text = "Please enter details below").pack()
  Label(screen2_2, text = "").pack()
  Label(screen2_2, text = "Username * ").pack()
  username_entry = Entry(screen2_2, textvariable = username)
  username_entry.pack()
  Label(screen2_2, text = "Password * ").pack()
  password_entry =  Entry(screen2_2, textvariable = password)
  password_entry.pack()
  Label(screen2_2, text = "").pack()
  Button(screen2_2, text = "Register", width = 10, height = 1,command=playgame_3).pack()

def nhaptien_3():
	root=Tk()
	label_1=Label(root,text="nhap so tien nap (1000~10000): ",fg="red",bg="white")
	entry_1=Entry(root)
	label_1.grid(row=0)
	entry_1.grid(row=0,column=1)
	label_2=Label(root,text="nhap so tien muon luu: ",fg="red",bg="white")
	entry_2=Entry(root)
	label_2.grid(row=1)
	entry_2.grid(row=1,column=1)
	bottomframe1=Frame(root)
	bottomframe1.grid(row=2)
	button7=Button(bottomframe1,text="play",command=playgame_3)
	button7.pack()
	root.mainloop()

def playgame_3():
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
	wn.exitonclick()
	close()

def close(): 
	#Result
	game.title("RESULT")
	#background
	screen = Canvas(master=game, width=500, height=400, background="pink")
	screen.pack()
	#khung
	rect = screen.create_rectangle(50,50,475,375, fill="white", outline="blue")
	screen.update()
	#ten
	text = screen.create_text(100,50,text ="Name:", fill="blue", font=("Arial", 15))
	text = screen.create_text(275,60,text ="name", fill="blue", font=("Arial", 15))
	#diem
	text = screen.create_text(100,150,text ="Score:", fill="blue", font=("Arial", 15))
	text = screen.create_text(250,200,text ="score", fill="Red", font=("Arial", 60))
	#loi chuc
	#text = screen.create_text(250,300, text = "Better Luck Next Time!!!", fill="green", font=("Times New Roman", 15))
	#button exit
	btn_exit = Button(game, text="Back", font=("Arial", 14, "bold"),bg="cyan", fg="green", width=10, height=1, command=manhinh1)
	btn_exit.pack()
	btn_exit.place(x=0,y=0)
	game.mainloop()
manhinh1()
