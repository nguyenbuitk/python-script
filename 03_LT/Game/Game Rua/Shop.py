from tkinter import *
game = Tk()
from functools import partial
import tkinter.messagebox
money=3000
def Buy(price):
	global money
		if money<price:
			tkinter.messagebox.showinfo('Sorry', 'You don\'t have enough money')

	else:
		money=money-price
		tkinter.messagebox.showinfo('', 'Success!')

def command1(price):
	global money
		if money<price:
		tkinter.messagebox.showinfo('Sorry', 'You don\'t have enough money')

	else:
		money=money-price
		tkinter.messagebox.showinfo('', 'Success!')
	return 1
def command2(price):
	global money
		if money<price:
		tkinter.messagebox.showinfo('Sorry', 'You don\'t have enough money')

	else:
		money=money-price
		tkinter.messagebox.showinfo('', 'Success!')
	return 2
def command3(price):
	global money
		if money<price:
		tkinter.messagebox.showinfo('Sorry', 'You don\'t have enough money')

	else:
		money=money-price
		tkinter.messagebox.showinfo('', 'Success!')
	return 3
def command4(price):
	global money
		if money<price:
		tkinter.messagebox.showinfo('Sorry', 'You don\'t have enough money')

	else:
		money=money-price
		tkinter.messagebox.showinfo('', 'Success!')
	return 4
def close(): 
	game.destroy()
game.title("SKIN SHOP")
screen = Canvas(master=game, width=750, height=400, background="cyan")
screen.pack()
#khung
rect = screen.create_rectangle(25,25,725,375, fill="white", outline="black")
screen.update()
rect = screen.create_rectangle(300,50,300,350, fill="white", outline="black")
screen.update()
rect = screen.create_rectangle(575,50,575,350, fill="white", outline="black")
screen.update()
text = screen.create_text(162,50,text ="Item", fill="purple", font=("Arial", 15))
text = screen.create_text(438,50,text ="Price", fill="purple", font=("Arial", 15))
text = screen.create_text(162,125,text ="Red skin", fill="red", font=("Bauhaus 93", 35, "bold"))
text = screen.create_text(438,125,text ="2000$", fill="red", font=("Bauhaus 93", 35, "bold"))
#second
text = screen.create_text(162,190,text ="Green skin", fill="Green", font=("Bauhaus 93", 35, "bold"))
text = screen.create_text(438,190,text ="2500$", fill="Green", font=("Bauhaus 93", 35, "bold"))
#third
text = screen.create_text(162,255,text ="Blue skin", fill="Blue", font=("Bauhaus 93", 35, "bold"))
text = screen.create_text(438,255,text ="3000$", fill="Blue", font=("Bauhaus 93", 35, "bold"))
text = screen.create_text(162,320,text ="Yellow skin", fill="Yellow", font=("Bauhaus 93", 35, "bold"))
text = screen.create_text(438,320,text ="3500$", fill="Yellow", font=("Bauhaus 93", 35, "bold"))
btn_buy1 = Button(master=game, text='Buy',width=10, height=2,command=partial(Buy,2000))
btn_buy1.place(x=600,y=105)
btn_buy2 = Button(master=game, text='Buy',width=10, height=2,command=partial(Buy,2500))
btn_buy2.place(x=600,y=170)
btn_buy3 = Button(master=game, text='Buy',width=10, height=2,command=partial(Buy,3000))
btn_buy3.place(x=600,y=235)
btn_buy4 = Button(master=game, text='Buy',width=10, height=2,command=partial(Buy,3500))
btn_buy4.place(x=600,y=300)
btn_exit = Button(master=game, text='BACK',width=10, height=1,command=close)
btn_exit.pack(side=RIGHT)
game.mainloop()
