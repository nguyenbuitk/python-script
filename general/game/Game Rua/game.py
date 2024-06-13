from tkinter import *
import turtle
from random import randint
root=Tk()

def playgame():
	tina = turtle.Turtle()
	tina.speed(100)
	tina.penup()
	tina.goto(-140,140)
	for step in range(16):
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

def nhaptien():
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
	button7=Button(bottomframe1,text="play",command=playgame)
	button7.pack()
	root.mainloop()

topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
#button: nút bấm
button1=Button(topframe,text="play game",command=nhaptien)
button2=Button(topframe,text="countinue")
button3=Button(topframe,text="help")
button4=Button(bottomframe,text="exit")


button4.pack()
button1.pack()
button2.pack()
button3.pack()

root.mainloop()