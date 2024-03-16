import random
import numpy as np
from tkinter import *
from functools import partial
import tkinter.messagebox
TotalScore=2900
def Minigame():
  fscreen= Tk()
  fscreen.geometry("300x500")
  fscreen.title("Minigame")
  Label(text = "Welcome!", width = "300", height = "2", font = ("Calibri", 18)).pack()
  Label(text = "").pack()
  Label(text = "Choose an option", bg = "cyan", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text="").pack()
  Button(text = "Play Turtlesweeper",height = "2", width = "30",command=partial(goto,fscreen,1)).pack()
  Label(text = "").pack()
  Button(text = "Scoreboard",height = "2", width = "30",command=partial(goto,fscreen,3)).pack()
  Label(text = "").pack()
  Button(text = "Exit",height = "2", width = "30",command=fscreen.destroy).pack()
  fscreen.mainloop()
def Choose_level_screen():
  screen = Tk()
  screen.geometry("300x500")
  screen.title("Choose level")
  Label(text = "Turtlesweeper", width = "300", height = "2", font = ("Calibri", 18)).pack()
  Label(text = "").pack()
  Label(text = "Which level you want to play?", bg = "cyan", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text="").pack()
  Button(text = "Very easy",height = "2", width = "30",command=partial(playgame,4,screen)).pack()
  Label(text = "").pack()
  Button(text = "Easy",height = "2", width = "30",command=partial(playgame,6,screen)).pack()
  Label(text = "").pack()
  Button(text = "Normal",height = "2", width = "30",command=partial(playgame,8,screen)).pack() 
  Label(text = "").pack()
  Button(text = "Hard",height = "2", width = "30",command=partial(playgame,10,screen)).pack() 
  Label(text = "").pack()
  Button(text = "Turn back",height = "2", width = "30",bg="cyan",command=partial(Turn_back,screen)).pack(fill=X)  
  screen.mainloop()
def Score_screen():
    sscreen=Tk()
    sscreen.geometry("300x500")
    sscreen.title("Score board")
    Label(text = "Your current score", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text=TotalScore).pack()
    Label(text = "Max score available", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text="3000").pack()
    
    Button(text = "Turn back",height = "2", width = "30",bg="cyan",command=partial(Turn_back,sscreen)).pack(fill=X)
    sscreen.mainloop()
def goto(root,a):
    close(root)
    if a==1:
        Choose_level_screen()
    else:
        Score_screen()
def Turn_back(root):
    close(root)
    Minigame()
def close(root):
    root.destroy()
def SumOfMines(A,x,y,size):
    for a in range(x-1,x+2):
        for b in range(y-1,y+2):
            if min(a,b)>=0 and max(a,b)<= size-1 and A[a][b]==9:
               A[x][y]=A[x][y]+1
    return A
        
def CreateBoard(size):
    A = np.zeros((size, size),dtype=int)
    mine=0
    while mine< int((size*size)/6):
        col=random.randint(0, size-1)
        row=random.randint(0, size-1)
        if(A[col][row]==0):
            A[col][row]=9
            mine=mine+1
    for x in range (size):
        for y in range (size):
            if A[x][y]==0:
                SumOfMines(A,x,y,size)
    return A

def DrawBoard(A,size,tk):
    btn_dict = {}
    for row in range (size):
        for col in range(size):
            btn_dict = Button(tk,bg="cyan",width=6,height=3,command=partial(ShowBox,A,row,col,tk,size)) 
            btn_dict.grid(row=row, column=col)
                           
            
def ShowBox(A,row,col,tk,size):
    if(A[row][col]==0):
        A[row][col]=-1
        btn=Button(tk,width=6,height=3,bg="blue",text="")
        btn.grid(row=row,column=col)
        for a in range(row-1,row+2):
            for b in range(col-1,col+2):
                if min(a,b)>=0 and max(a,b)<= size-1 and A[a][b]!=9 and A[a][b]!=-1:
                   ShowBox(A,a,b,tk,size)
        
    elif(A[row][col]!=9):
            btn=Button(tk,width=6,height=3,text=A[row][col],bg="yellow")
            btn.grid(row=row,column=col)
            A[row][col]=-1
    else:
        btn=Button(tk,width=6,height=3,text=":(",bg="red")
        btn.grid(row=row,column=col)
        tkinter.messagebox.showinfo('Sorry', 'You lost the game')
        ans=tkinter.messagebox.askquestion('Replay', 'Do you wish to play again')
        close(tk)
        if ans=='yes':
            Choose_level_screen()
        
    if isGameWinned(A,size):
        size+=1
        tkinter.messagebox.showinfo('Congratulation', 'You won the game and got some points')
        global TotalScore
        TotalScore+= size*size
        ans=tkinter.messagebox.askquestion('Replay', 'Do you wish to play again')
        close(tk)
        if ans=='yes':
            Choose_level_screen()
            
def isGameWinned(A,size):
    count=0
    size2=size*size
    for x in range(size):
        for y in range(size):
            if A[x][y]==-1:
                count+=1
    return (count==size2-int(size2/6))
    
def playgame(size,root):
    close(root)
    tk=Tk()
    tk.title("Turtlesweeper")
    global TotalScore
    if TotalScore > 3000:
      tkinter.messagebox.showinfo('Sorry', 'Your score is over 3000, try again later if you don\'t have enough money')
      close(tk)
    else:
      board=CreateBoard(size)
      #print(board)
      DrawBoard(board,size,tk)
    tk.mainloop()

Minigame()
