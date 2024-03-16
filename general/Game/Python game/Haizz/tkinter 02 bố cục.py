from tkinter import *

#tạo màn hình tk
root=Tk()
#frame= khung
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
#button: nút bấm
button1=Button(topframe,text="play game")
button2=Button(topframe,text="countinue")
button3=Button(topframe,text="help")
button4=Button(bottomframe,text="exit")


button4.pack()
button1.pack()
button2.pack()
button3.pack()

root.mainloop()