
import turtle
from tkinter import *
from random import randint

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


#red.right(36)
#for i in range(10):
     #red.forward(5)
     #red.right(5.4)
     #red.forward(randint(1,5))


wn=turtle.Screen()
wn.exitonclick()