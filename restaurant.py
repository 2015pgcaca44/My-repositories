from tkinter import *
import random
import time;
win=Tk()
win.geometry("1600x800+0+0")
win.title("Restaurant Management System")
#l=Label(win,text="hello world",fg="red",bg="skyblue")
#l.pack()
text_Input=StringVar()
operator=""

tops = Frame(win,width=1600,height=50,bg="powder blue",relief=SUNKEN)
tops.pack(side=TOP)

f1 = Frame(win,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(win,width=300,height=700,bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

l1=Label(tops,text="Restaurant Management System",fg="Steel Blue",bd=5,font=('arial',30,'bold'))
l1.grid(row=0,column=0)
 
l1=Label(tops,text=localtime,fg="Steel Blue",bd=5,font=('arial',10,'bold'))
l1.grid(row=1,column=0)
#-----------------------------f1 code -------------------------------
def btnclick(num):
   global operator
   operator=operator+str(num)
   text_Input.set(operator)

def btnclar():
   global operator
   operator=""
   text_Input.set("")

def btnequi():
   global operator
   equal=str(eval(operator))
   text_Input.set(equal)
   operator=""

def btnref():   
   x=random.randint(1000,99999)
   refer=str(x)
   rand.set(refer)
   
def btnexit():
   win.destroy()

def btnreset():
   rand.set("")
   fries.set("")
   burger.set("")
   chicken.set("")
   cheese.set("")
   total.set("")
   sub_total.set("")
   drink.set("")
   statetax.set("")
   pastry.set("")
   servicecharge.set("")
   
#-----------------------------------------------------------------------------------------------------------------
txtdisp=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=15,insertwidth=4,bg="powder blue",justify='right')
txtdisp.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="7",command=lambda:btnclick(7))
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="8",command=lambda:btnclick(8))
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="9",command=lambda:btnclick(9))
btn9.grid(row=2,column=2)

btnplus=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="+",command=lambda:btnclick("+"))
btnplus.grid(row=2,column=3)

btn4=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="4",command=lambda:btnclick(4))
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="5",command=lambda:btnclick(5))
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="6",command=lambda:btnclick(6))
btn6.grid(row=3,column=2)

btnminus=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="-",command=lambda:btnclick("-"))
btnminus.grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="1",command=lambda:btnclick(1))
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="2",command=lambda:btnclick(2))
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="3",command=lambda:btnclick(3))
btn3.grid(row=4,column=2)

btnmul=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="*",command=lambda:btnclick("*"))
btnmul.grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="0",command=lambda:btnclick("0"))
btn0.grid(row=5,column=0)

btnclear=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="C",command=lambda:btnclar())
btnclear.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="=",command=lambda:btnequi())
btnequal.grid(row=5,column=2)

btndiv=Button(f2,padx=16,pady=16,bd=10,bg="powder blue",font=('arial',20,'bold'),text="/",command=lambda:btnclick("/"))
btndiv.grid(row=5,column=3)
            
#----------------------------------------------f2 code-------------------------------------------------------------
rand=StringVar()
fries=StringVar()
burger=StringVar()
chicken=StringVar()
cheese=StringVar()
total=StringVar()
sub_total=StringVar()
drink=StringVar()
statetax=StringVar()
pastry=StringVar()
servicecharge=StringVar()
l1=Label(f1,font=('arial',20,'bold'),text="Reference",bd=15)
l1.grid(row=0,column=0)
txtl1=Entry(f1,font=('arial',20,'bold'),textvariable=rand,insertwidth=4,bg="powder blue",justify='right')
txtl1.grid(row=0,column=1)

l2=Label(f1,font=('arial',20,'bold'),text="Fries",bd=15)
l2.grid(row=1,column=0)
txtl2=Entry(f1,font=('arial',20,'bold'),textvariable=fries,insertwidth=4,bg="powder blue",justify='right')
txtl2.grid(row=1,column=1)

l3=Label(f1,font=('arial',20,'bold'),text="Burger",bd=15)
l3.grid(row=2,column=0)
txtl3=Entry(f1,font=('arial',20,'bold'),textvariable=burger,insertwidth=4,bg="powder blue",justify='right')
txtl3.grid(row=2,column=1)

l4=Label(f1,font=('arial',20,'bold'),text="Chicken",bd=15)
l4.grid(row=3,column=0)
txtl4=Entry(f1,font=('arial',20,'bold'),textvariable=chicken,insertwidth=4,bg="powder blue",justify='right')
txtl4.grid(row=3,column=1)

l5=Label(f1,font=('arial',20,'bold'),text="Cheese",bd=15)
l5.grid(row=4,column=0)
txtl5=Entry(f1,font=('arial',20,'bold'),textvariable=cheese,insertwidth=4,bg="powder blue",justify='right')
txtl5.grid(row=4,column=1)

l6=Label(f1,font=('arial',20,'bold'),text="Drink",bd=15)
l6.grid(row=5,column=0)
txtl6=Entry(f1,font=('arial',20,'bold'),textvariable=drink,insertwidth=4,bg="powder blue",justify='right')
txtl6.grid(row=5,column=1)

l7=Label(f1,font=('arial',20,'bold'),text="Pastry",bd=15)
l7.grid(row=0,column=2)
txtl7=Entry(f1,font=('arial',20,'bold'),textvariable=pastry,insertwidth=4,bg="powder blue",justify='right')
txtl7.grid(row=0,column=3)

l8=Label(f1,font=('arial',20,'bold'),text="State Tax",bd=15)
l8.grid(row=1,column=2)
txtl8=Entry(f1,font=('arial',20,'bold'),textvariable=statetax,insertwidth=4,bg="powder blue",justify='right')
txtl8.grid(row=1,column=3)

l9=Label(f1,font=('arial',20,'bold'),text="Sub total",bd=15)
l9.grid(row=2,column=2)
txtl9=Entry(f1,font=('arial',20,'bold'),textvariable=sub_total,insertwidth=4,bg="powder blue",justify='right')
txtl9.grid(row=2,column=3)

l10=Label(f1,font=('arial',20,'bold'),text="Service Tax",bd=15)
l10.grid(row=3,column=2)
txtl10=Entry(f1,font=('arial',20,'bold'),textvariable=servicecharge,insertwidth=4,bg="powder blue",justify='right')
txtl10.grid(row=3,column=3)

l11=Label(f1,font=('arial',20,'bold'),text="Tatal Cost",bd=15)
l11.grid(row=4,column=2)
txtl11=Entry(f1,font=('arial',20,'bold'),textvariable=total,insertwidth=4,bg="powder blue",justify='right')
txtl11.grid(row=4,column=3)

#----------------------------------buttons-------------------------------------------------------------

btntotal=Button(f1,padx=16,pady=8,bd=10,width=5,bg="powder blue",font=('arial',15,'bold'),text="Refer",command=btnref)
btntotal.grid(row=7,column=1)

btnrst=Button(f1,padx=16,pady=8,bd=10,width=5,bg="powder blue",font=('arial',15,'bold'),text="Reset",command=btnreset)
btnrst.grid(row=7,column=2)

btnquit=Button(f1,padx=16,pady=8,bd=10,width=5,bg="powder blue",font=('arial',15,'bold'),text="Exit",command=btnexit)
btnquit.grid(row=7,column=3)

win.mainloop()

 
 
