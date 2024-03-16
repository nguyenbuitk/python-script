import random
import numpy as np
from tkinter import *
from functools import partial
import tkinter.messagebox

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
        btn=Button(tk,width=6,height=3,bg="blue")
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
        btn=Button(tk,width=6,height=3,bg="red",text="mine")
        btn.grid(row=row,column=col)
        tkinter.messagebox.showinfo('Sorry', 'You lost the game')
        close(tk)
    if isGameWinned(A,size):
        tkinter.messagebox.showinfo('Congratulation', 'You won the game')
        #score+= size*size
        close(tk)
            
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
    board=CreateBoard(size)
    #print(board)
    tk=Tk()
    DrawBoard(board,size,tk)
    tk.mainloop()
    
    
