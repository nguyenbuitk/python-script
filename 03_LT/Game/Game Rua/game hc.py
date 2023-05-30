def VaChamBua(xcor,xbua):#Khi rua an khi bua
    if (xcor>=xbua)&(xcor<=4+xbua):return 1
    else:return 0	

def chonshape(chonshape,shape,shape1):
    if chonshape==0:shape="turtle";shape="turtle"
    if chonshape==1:shape="car.gif";shape1="car1.gif"
    if chonshape==2:shape="rocket.gif";shape1="rocket1.gif"
    if chonshape==3:shape="motobike";shape1="motobike1"
        



def sinhbua(xcor,ycor,loaibua,buaT,buaG,buaR,buaW,buaD,buaQ):
    if loaibua==1:buaT.goto(xcor,ycor);buaT.st()
    if loaibua==2:buaG.goto(xcor,ycor);buaG.st()
    if loaibua==5:buaR.goto(xcor,ycor);buaR.st()
    if loaibua==4:buaW.goto(xcor,ycor);buaW.st()
    if loaibua==3:buaD.goto(xcor,ycor);buaD.st()
    if loaibua==6:buaQ.goto(xcor,ycor);buaQ.st()
    
    
def playgame():
    win=turtle.Screen()
    chondang=0
    if chondang>3:
            if chondang==4:win.bgpic("re.gif")
            if chondang==5:win.bgic("giphy.gif")
    win.update()
    
    win.setup(1300,700)
    win.bgcolor("white")
    
    #RUAAAAAAAAAAAAAAAAAAAAAAAAAAA=============================RUUUUUUUUUUUUUUUUUUUUUUUUUAAAAAAAAAAAAA
    shape="turtle"
    shape1="turtle"
    
    if chondang!=0:
        if chondang==1:shape="car.gif";shape1="car1.gif"
        if chondang==2:shape="rocket.gif";shape1="rocket1.gif"
        if chondang==3:shape="moto.gif";shape1="moto1.gif"
        win.addshape(shape)
        win.addshape(shape1)
    red_height=arr.array("i",[930,830,730,630])

    red=turtle.Turtle()
    red.color("red")
    red.shape(shape)
    red.penup()
    red.goto(-129.5,-232.5)
    red.speed(100)

    blue=turtle.Turtle()
    blue.color("blue")
    blue.shape(shape)
    blue.penup()
    blue.goto(-179.5,-207.5)
    blue.speed(100)

    yellow=turtle.Turtle()
    yellow.color("yellow")
    yellow.shape(shape)
    yellow.penup()
    yellow.goto(-232.5,-182.5)

    yellow.speed(100)
    black=turtle.Turtle()
    black.color("black")
    black.shape(shape)
    black.penup()
    black.goto(-272.5,-157.5)

    black.speed(100)


       #Đường Đua-------------------------------------------------------
    tina = turtle.Turtle()
    letter_height=980
    letter_width=10
    space_width=1
    tina.penup()
    tina.goto(-600,0)
    tina.speed(100)
    tina.right(90)
    for step in range(5):
        tina.write(step,align='center');
        #tina.left(90);
        #tina.forward(10);
        tina.pendown();
   
        tina.circle(letter_height/4, 90)
        tina.forward(letter_height/2)
        tina.circle(letter_height/4, 90)
        tina.circle(letter_height/4, 90)
        tina.forward(letter_height/2)
        if step==4:
            tina.right(90)
            tina.forward(100)
            tina.penup()
            tina.backward(100)
            tina.left(90)
            tina.pendown()
        tina.circle(letter_height/4, 90)
        tina.penup()
        tina.left(90)
        tina.forward(50)
        tina.right(90)
        letter_height-=100
    ############################### CAC BIEN DIEM
    reddem=214
    bluedem=141
    yellowdem=68
    blackdem=0
    letter_height=980
    # Cac loai bua-------------------------------------#
    #####################################################   TANG TOC
    buaT=turtle.Turtle()
    buaT.ht()  #Bua tang toc
    buaT.color("green")
    buaT.shape("triangle")    
    buaT.speed(100)
    buaT.penup()
    
    
    buaT1=turtle.Turtle()
    buaT1.ht()  #Bua tang toc
    buaT1.color("green")
    buaT1.shape("triangle")    
    buaT1.speed(100)
    buaT1.penup()
    
    
    buaT2=turtle.Turtle()
    buaT2.ht()  #Bua tang toc
    buaT2.color("green")
    buaT2.shape("triangle")    
    buaT2.speed(100)
    buaT2.penup()
    
    
    buaT3=turtle.Turtle()
    buaT3.ht()  #Bua tang toc
    buaT3.color("green")
    buaT3.shape("triangle")    
    buaT3.speed(100)
    buaT3.penup()
    
   #####################################################   GIAM TOC
   
    buaG=turtle.Turtle() 
    buaG.ht()   #bùa Giảm tốc
    buaG.color("black")
    buaG.shape("triangle")
    buaG.speed(100)
    buaG.penup()
    
        
    buaG1=turtle.Turtle()
    buaG1.ht()    #bùa Giảm tốc
    buaG1.color("black")
    buaG1.shape("triangle")
    buaG1.speed(100)
    buaG1.penup()
    
        
    buaG2=turtle.Turtle() 
    buaG2.ht()   #bùa Giảm tốc
    buaG2.color("black")
    buaG2.shape("triangle")
    buaG2.speed(100)
    buaG2.penup()
    
        
    buaG3=turtle.Turtle() 
    buaG3.ht()   #bùa Giảm tốc
    buaG3.color("black")
    buaG3.shape("triangle")
    buaG3.speed(100)
    buaG3.penup()
    
    #################################################### QUAY VE VI TRI BAN DAU
    buaR=turtle.Turtle() 
    buaR.ht()  #bùa quay lại vị trí ban đầu
    buaR.color("black")
    buaR.shape("square")
    buaR.speed(100)
    buaR.penup()
    
    
    buaR1=turtle.Turtle() 
    buaR1.ht()  #bùa quay lại vị trí ban đầu
    buaR1.color("black")
    buaR1.shape("square")
    buaR1.speed(100)
    buaR1.penup()
    

    buaR2=turtle.Turtle() 
    buaR2.ht()  #bùa quay lại vị trí ban đầu
    buaR2.color("black")
    buaR2.shape("square")
    buaR2.speed(100)
    buaR2.penup()
    

    buaR3=turtle.Turtle() 
    buaR3.ht()  #bùa quay lại vị trí ban đầu
    buaR3.color("black")
    buaR3.shape("square")
    buaR3.speed(100)
    buaR3.penup()
    
    ############################################################# VE DICH

    buaW=turtle.Turtle()
    buaW.ht()   #bùa chiến thắng
    buaW.color("Green")
    buaW.shape("square")
    buaW.speed(100)
    buaW.penup()
    

    buaW1=turtle.Turtle() 
    buaW1.ht()  #bùa chiến thắng
    buaW1.color("Green")
    buaW1.shape("square")
    buaW1.speed(100)
    buaW1.penup()
    
     
    buaW2=turtle.Turtle() 
    buaW2.ht()  #bùa chiến thắng
    buaW2.color("Green")
    buaW2.shape("square")
    buaW2.speed(100)
    buaW2.penup()
    
     
    buaW3=turtle.Turtle() 
    buaW3.ht()  #bùa chiến thắng
    buaW3.color("Green")
    buaW3.shape("square")
    buaW3.speed(100)
    buaW3.penup()
    

    ########################################################## QUAY DAU

    buaQ=turtle.Turtle() 
    buaQ.ht()  #bùa quay đầu
    buaQ.color("Black")
    buaQ.shape("circle")
    buaQ.speed(100)
    buaQ.penup()   
    
    
    buaQ1=turtle.Turtle() 
    buaQ1.ht()  #bùa quay đầu
    buaQ1.color("Black")
    buaQ1.shape("circle")
    buaQ1.speed(100)
    buaQ1.penup()   
    
    
    buaQ2=turtle.Turtle()  
    buaQ2.ht() #bùa quay đầu
    buaQ2.color("Black")
    buaQ2.shape("circle")
    buaQ2.speed(100)
    buaQ2.penup()   
    
    
    buaQ3=turtle.Turtle() 
    buaQ3.ht()  #bùa quay đầu
    buaQ3.color("Black")
    buaQ3.shape("circle")
    buaQ3.speed(100)
    buaQ3.penup()   
    
    #################################################### DUNG CHAN

    buaD=turtle.Turtle() 
    buaD.ht()  #bùa dừng chân
    buaD.color("Black")
    buaD.shape("classic")
    buaD.speed(100)
    buaD.penup()
    

    buaD1=turtle.Turtle()  
    buaD1.ht() #bùa dừng chân
    buaD1.color("Black")
    buaD1.shape("classic")
    buaD1.speed(100)
    buaD1.penup()
    

    buaD2=turtle.Turtle()  
    buaD2.ht() #bùa dừng chân
    buaD2.color("Black")
    buaD2.shape("classic")
    buaD2.speed(100)
    buaD2.penup()
    

    buaD3=turtle.Turtle()  
    buaD3.ht() #bùa dừng chân
    buaD3.color("Black")
    buaD3.shape("classic")
    buaD3.speed(100)
    buaD3.penup()
    



    Flag=arr.array("i",[2000,2000,2000,2000])
    flagred=arr.array("i",[0,0,0,0])
    Flagred=arr.array("i",[70,70,70,70])
    dich=850 #Đích----------
    ketqua=0
    redcount1=10
    redcount2=-1
    bluecount1=10
    bluecount2=-1
    yellowcount1=10
    yellowcount2=-1
    blackcount1=10
    blackcount2=-1
    loaibua=arr.array("i",[0,0,0,0])
    toadox=arr.array("i",[0,0,0,0])
    
    winsound.PlaySound("Theme.wav",winsound.SND_ASYNC)
    for run in range(1000): #Chuong trinh Rua chay
        if redcount1==0:
           loaibua[0]=randint(1,3)
           buaT.ht()
           buaG.ht()
           buaD.ht()
           toadox[0]=randint(-100,100)
           sinhbua(toadox[0],-232.5,loaibua[0],buaT,buaG,buaR,buaW,buaD,buaQ)
           redcount1=30
        else: redcount1-=1
        if redcount2==1:
           buaW.ht()
           buaR.ht()
           buaQ.ht()
           loaibua[0]=randint(4,20)
           if (loaibua[0]>=9):loaibua[0]=6
           toadox[0]=randint(-250,110)
           sinhbua(toadox[0],233,loaibua[0],buaT,buaG,buaR,buaW,buaD,buaQ)
           redcount2=30
        else: redcount2-=1
        #----------------------------------------------------#Xử lý ăn bùa
        dem=randint(2,4)
        if (VaChamBua(red.xcor(),toadox[0]))&(loaibua[0]==1):dem=randint(10,20);buaT.ht()     #bùa tăng tốc 
        if (VaChamBua(red.xcor(),toadox[0]))&(loaibua[0]==2):dem=1;buaG.ht()         #bùa giảm tốc
        if (VaChamBua(red.xcor(),toadox[0]))&(loaibua[0]==5):               #bua quay lại vị trí ban đầu
            reddem=0;
            red.goto(-129.5,-232.5);buaR.ht()
            red.right(180)
            red.shape(shape)  
        if (VaChamBua(red.xcor(),toadox[0]))&(loaibua[0]==4):#bùa về đích
            reddem=dich
            red.goto(-272.5,red.ycor());
            dem=0
        if (VaChamBua(red.xcor(),toadox[0]))&(loaibua[0]==3):Flagred[0]=reddem;buaD.ht();Flagred[0]=-90   #bùa dừng chân
        if Flagred[0]<-70:dem=0;Flagred[0]+=2
        if (VaChamBua(red.xcor(),toadox[0]))&(loaibua[0]==6):Flag[0]=reddem;reddem=reddem-50;red.left(180);red.shape(shape);buaQ.ht(); 
        if VaChamBua(reddem,Flag[0]):red.left(180);Flag[0]=2000;red.shape(shape1)  
        #-----------------------------------------------------------#Xư lý ăn bùa
        red.forward(dem)
        reddem+=dem
        if (reddem>=(red_height[0]/2))&(flagred[0]<18):
            red.shape(shape1)  #doi chieu icon
            redcount1=-1
            redcount2=20
            red.left(10)
            red.forward(38)
            flagred[0]+=1
        if reddem>=850:ketqua=1;break;
  
 #Rua Xanh----------------------------------------      
        if bluecount1==0:
           loaibua[1]=randint(1,3)
           buaT1.ht()
           buaG1.ht()
           buaD1.ht()
           toadox[1]=randint(-200,100)
           sinhbua(toadox[1],-207.5,loaibua[1],buaT1,buaG1,buaR1,buaW1,buaD1,buaQ1)
           bluecount1=30
        else: bluecount1-=1
        if bluecount2==1:
           buaW1.ht()
           buaR1.ht()
           buaQ1.ht()
           loaibua[1]=randint(4,20)
           if (loaibua[1]>=9):loaibua[1]=6
           toadox[1]=randint(-250,110)
           sinhbua(toadox[1],206,loaibua[1],buaT1,buaG1,buaR1,buaW1,buaD1,buaQ1)
           bluecount2=20
        else: bluecount2-=1
        #----------------------------------------------------#Xử lý ăn bùa
        dem=randint(2,4)
        if (VaChamBua(blue.xcor(),toadox[1]))&(loaibua[1]==1):dem=randint(10,20);buaT1.ht()     #bùa tăng tốc 
        if (VaChamBua(blue.xcor(),toadox[1]))&(loaibua[1]==2):dem=1;buaG1.ht()         #bùa giảm tốc
        if (VaChamBua(blue.xcor(),toadox[1]))&(loaibua[1]==5):               #bua quay lại vị trí ban đầu
            bluedem=0;
            blue.goto(-179.5,-207.5);buaR1.ht()
            blue.shape(shape)
            blue.right(180)
        if (VaChamBua(blue.xcor(),toadox[1]))&(loaibua[1]==4):#bùa về đích
            bluedem=dich
            blue.goto(-272.5,blue.ycor());
            dem=0
        if (VaChamBua(blue.xcor(),toadox[1]))&(loaibua[1]==3):Flagred[1]=bluedem;buaD1.ht();Flagred[1]=-90   #bùa dừng chân
        if Flagred[1]<-70:dem=0;Flagred[1]+=2
        if (VaChamBua(blue.xcor(),toadox[1]))&(loaibua[1]==6):Flag[1]=bluedem;bluedem=bluedem-50;blue.left(180);buaQ1.ht();blue.shape(shape)
        if VaChamBua(bluedem,Flag[1]):blue.left(180);Flag[1]=2000;blue.shape(shape1)
        #-----------------------------------------------------------#Xư lý ăn bùa
        blue.forward(dem)
        bluedem+=dem
        if (bluedem>=(red_height[1]/2))&(flagred[1]<18):
            blue.shape(shape1)
            bluecount1=-1
            bluecount2=20
            blue.left(10)
            blue.forward(33.5)
            flagred[1]+=1
        if bluedem>=850-75:ketqua=2;break;
  
  #Rua Vang----------------------------------------     
        if yellowcount1==0:
           loaibua[2]=randint(1,3)
           buaT2.ht()
           buaG2.ht()
           buaD2.ht()
           toadox[2]=randint(-200,100)
           sinhbua(toadox[2],-179.5,loaibua[2],buaT2,buaG2,buaR2,buaW2,buaD2,buaQ2)
           yellowcount1=25
        else: yellowcount1-=1
        if yellowcount2==1:
           buaW2.ht()
           buaR2.ht()
           buaQ2.ht()
           loaibua[2]=randint(4,20)
           if (loaibua[2]>=9):loaibua[2]=6
           toadox[2]=randint(-250,110)
           sinhbua(toadox[2],180,loaibua[2],buaT2,buaG2,buaR2,buaW2,buaD2,buaQ2)
           yellowcount2=22
        else: yellowcount2-=1
        #----------------------------------------------------#Xử lý ăn bùa
        dem=randint(2,4)
        if (VaChamBua(yellow.xcor(),toadox[2]))&(loaibua[2]==1):dem=randint(10,20);buaT2.ht()     #bùa tăng tốc 
        if (VaChamBua(yellow.xcor(),toadox[2]))&(loaibua[2]==2):dem=1;buaG2.ht()         #bùa giảm tốc
        if (VaChamBua(yellow.xcor(),toadox[2]))&(loaibua[2]==5):               #bua quay lại vị trí ban đầu
            yellowdem=0;
            yellow.goto(-232.5,-182.5);buaR2.ht()
            yellow.shape(shape)
            yellow.right(180)
        if (VaChamBua(yellow.xcor(),toadox[2]))&(loaibua[2]==4):#bùa về đích
            yellowdem=dich
            yellow.goto(-272.5,yellow.ycor());
            dem=0
        if (VaChamBua(yellow.xcor(),toadox[2]))&(loaibua[2]==3):Flagred[2]=yellowdem;buaD2.ht();Flagred[2]=-90   #bùa dừng chân
        if Flagred[2]<-70:dem=0;Flagred[2]+=2
        if (VaChamBua(yellow.xcor(),toadox[2]))&(loaibua[2]==6):Flag[2]=yellowdem;yellowdem=yellowdem-50;yellow.left(180);buaQ2.ht();yellow.shape(shape)
        if VaChamBua(yellowdem,Flag[2]):yellow.left(180);Flag[2]=2000;yellow.shape(shape1)
        #-----------------------------------------------------------#Xư lý ăn bùa
        yellow.forward(dem)
        yellowdem+=dem
        if (yellowdem>=(red_height[2]/2))&(flagred[2]<18):
            yellow.shape(shape1)
            yellowcount1=-1
            yellowcount2=10
            yellow.left(10)
            yellow.forward(29)
            flagred[2]+=1
        if yellowdem>=850-75*2:ketqua=3;break;
  
        
   #Rua Den-------------------------------------------   
        if blackcount1==0:
           loaibua[3]=randint(1,3)
           buaT3.ht()
           buaG3.ht()
           buaD3.ht()
           toadox[3]=randint(-200,50)
           sinhbua(toadox[3],-157.5,loaibua[3],buaT3,buaG3,buaR3,buaW3,buaD3,buaQ3)
           blackcount1=26
        else: blackcount1-=1
        if blackcount2==1:
           buaW3.ht()
           buaR3.ht()
           buaQ3.ht()
           loaibua[3]=randint(4,20)
           if (loaibua[3]>=9):loaibua[3]=6
           toadox[3]=randint(-250,110)
           sinhbua(toadox[3],154,loaibua[3],buaT3,buaG3,buaR3,buaW3,buaD3,buaQ3)
           blackcount2=25
        else: blackcount2-=1
        #----------------------------------------------------#Xử lý ăn bùa
        dem=randint(2,4)
        if (VaChamBua(black.xcor(),toadox[3]))&(loaibua[3]==1):dem=randint(10,20);buaT3.ht()     #bùa tăng tốc 
        if (VaChamBua(black.xcor(),toadox[3]))&(loaibua[3]==2):dem=1;buaG3.ht()         #bùa giảm tốc
        if (VaChamBua(black.xcor(),toadox[3]))&(loaibua[3]==5):               #bua quay lại vị trí ban đầu
            blackdem=0;
            black.goto(-272.5,-157.5);buaR3.ht()
            black.shape(shape)
            black.right(180)
        if (VaChamBua(black.xcor(),toadox[3]))&(loaibua[3]==4):#bùa về đích
            blackdem=dich
            black.goto(-272.5,black.ycor());
            dem=0
        if (VaChamBua(black.xcor(),toadox[3]))&(loaibua[3]==3):Flagred[3]=blackdem;buaD3.ht();Flagred[3]=-90   #bùa dừng chân
        if Flagred[3]<-70:dem=0;Flagred[3]+=2
        if (VaChamBua(black.xcor(),toadox[3]))&(loaibua[3]==6):Flag[3]=blackdem;blackdem=blackdem-50;black.left(180);buaQ3.ht();black.shape(shape)
        if VaChamBua(blackdem,Flag[3]):black.left(180);Flag[3]=2000;black.shape(shape1)
        #-----------------------------------------------------------#Xư lý ăn bùa
        black.forward(dem)
        blackdem+=dem
        if (blackdem>=(red_height[3]/2))&(flagred[3]<18):
            black.shape(shape1)
            blackcount1=-1
            blackcount2=10
            black.left(10)
            black.forward(24.5)
            flagred[3]+=1
        if blackdem>=850-75*3:ketqua=4;break;

         #chien thang--------------------------------------------------------#
        if ketqua==1:red.circle(180);
        if ketqua==2:blue.circle(180);
        if ketqua==3:yellow.circle(180);
        if ketqua==4:black.circle(180);
    def Namewinner(kq):
        if kq==1:red.circle(180);return "Turtle 1";
        if kq==2:blue.circle(180);return "Turtle 2";
        if kq==3:yellow.circle(180);return "Turtle 3";
        if kq==4:black.circle(180);return "Turtle 4";
    chosenone=1
    name =Namewinner(ketqua)
    if ketqua==chosenone:
        score=100
    else:
        score=100-20
    game = Tk()
    def close(): 
         exit()
    #Result
    game.title("RESULT")
                    #                              winsound.PlaySound("endgame.wav",winsound.SND_ASYNC)
    
    #background
    screen = Canvas(master=game, width=500, height=400, background="pink")
    screen.pack()
    #khung
    rect = screen.create_rectangle(25,25,475,375, fill="white", outline="blue")
    screen.update()
    #ten
    text = screen.create_text(100,50,text ="Name:", fill="blue", font=("Arial", 15))
    text = screen.create_text(275,60,text =name, fill="blue", font=("Arial", 15))
    #diem
    text = screen.create_text(100,150,text ="Score:", fill="green", font=("Arial", 15))
    text = screen.create_text(250,200,text =score, fill="Red", font=("Arial", 60))

    #loi chuc
    #text = screen.create_text(250,300, text = "Better Luck Next Time!!!", fill="green", font=("Times New Roman", 15))
    #button exit
    btn_exit = Button(master=game, text='Exit', font=("Arial", 14, "bold"),bg="black", fg="green", width=10, height=1, command=close)
    btn_exit.pack()
    btn_exit.place(x=0,y=0)
    game.mainloop()  

       


    





    win.exitonclick()