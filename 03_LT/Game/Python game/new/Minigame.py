from tkinter import *
from functools import partial
from Turtlesweeper import playgame
from turtlerush import main
def firstscreen():
  fscreen= Tk()
  fscreen.geometry("300x500")
  fscreen.title("Minigame")
  Label(text = "Welcome!", width = "300", height = "2", font = ("Calibri", 18)).pack()
  Label(text = "").pack()
  Label(text = "Which game do you want to play?", bg = "cyan", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text="").pack()
  Button(text = "Turtle sweeper",height = "2", width = "30",command=partial(goto,fscreen,1)).pack()
  Label(text = "").pack()
  Button(text = "Turtle rush",height = "2", width = "30",command=partial(goto,fscreen,2)).pack()
  Label(text = "").pack()
  Button(text = "Scoreboard",height = "2", width = "30",command=partial(goto,fscreen,3)).pack()
  Label(text = "").pack()
  Button(text = "Exit",height = "2", width = "30",command=fscreen.destroy).pack()
  fscreen.mainloop()
def Choose_level_screen():
  screen = Tk()
  screen.geometry("300x500")
  screen.title("Choose level")
  Label(text = "Mine Sweeper", width = "300", height = "2", font = ("Calibri", 18)).pack()
  Label(text = "").pack()
  Label(text = "Which level you want to play?", bg = "cyan", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text="").pack()
  Button(text = "Very easy",height = "2", width = "30",command=partial(playgame,4,screen)).pack()
  Label(text = "").pack()
  Button(text = "Easy",height = "2", width = "30",command=partial(playgame,6,screen)).pack()
  Label(text = "").pack()
  Button(text = "Normal",height = "2", width = "30",command=partial(playgame,8,screen)).pack() 
  Label(text = "").pack()
  Button(text = "Turn back",height = "2", width = "30",bg="cyan",command=partial(Turn_back,screen)).pack(fill=X)  
  screen.mainloop()
def Score_screen():
    sscreen=Tk()
    sscreen.geometry("300x500")
    sscreen.title("Score board")
    Label(text = "Your highest score", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text="").pack()
    Label(text = "Your sum of score", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text = "Turn back",height = "2", width = "30",bg="cyan",command=partial(Turn_back,sscreen)).pack(fill=X)
    sscreen.mainloop()
def goto(root,a):
    close(root)
    if a==1:
        Choose_level_screen()
    elif a==2 :
        main()
    else:
        Score_screen()
def Turn_back(root):
    close(root)
    firstscreen()
def close(root):
    root.destroy()
def Minigame():
    firstscreen()
    

Minigame()
