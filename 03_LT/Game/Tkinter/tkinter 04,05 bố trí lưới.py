from tkinter import *
root=Tk()
label_1=Label(root,text="name")
label_2=Label(root,text="password")

#entry : ô trống

entry_1=Entry(root)
entry_2=Entry(root)
# sticky: căn chỉnh East ,West: trái ,phải
label_1.grid(row=0,sticky=E) 
label_2.grid(row=1)
#nếu dùng label_1.pack() thì sẽ bị lỗi
#
entry_1.grid(row=0,column=1)
entry_2.grid(row=3,column=1)

c=Checkbutton(root,text="nho ten dang nhap")
c.grid(columnspan=2)

root.mainloop()
