from tkinter import *
import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo('window title','mokwy cn ....')

answer=tkinter.messagebox.askquestion('question 1','do you like')

if answer=='yes':
	print(' fuck you')
