Label: tạo nhãn : Label(root,...)
frame : khung : Frame(root,...)
button : nút bấm: Button(frame,text="fadsf")
entry:ô trống để nhập: Entry(root)
entry1.grid:vị trí khung trống: entry.grid(row=343,column=32)

#tạo nút bấm tích v:
c=Checkbutton(root,text="nho ten dang nhap")
c.grid(columnspan=2)

#chức năng khi bấm vào button
button1=Button(topframe,text="play game",command=nhaptien)

#tạo nút bấm chuột trái,phải
frame=Frame(root,width=300,height=250)
frame.bind("<Button-1>",leftclick)
