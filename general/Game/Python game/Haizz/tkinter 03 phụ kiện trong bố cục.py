from tkinter import *
root =Tk()
#bg=background

one=Label(root,text="one")
one.pack()
two=Label(root,text="two",bg="green",fg="black")
#bôi cả dòng màu background
two.pack(fill=X)

three=Label(root,text="three")
three.pack(side=RIGHT,fill=Y)
root.mainloop()