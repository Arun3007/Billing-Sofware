from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import random
import datetime
win=Tk()
win.config(bg="#3deb34")
win.geometry=("1350x500+0+0")
win.title('Quastech Student Canteen')
# --------------------------frames------------------------------------------------------
mframe=Frame(win,height=100,width=1350,bd=10,relief="raise",bg="#3deb34")
mframe.pack(side=TOP)
lbtitle=Label(mframe,font=("arial",50,'bold'),text="\tQuastech Student Canteen\t\t\t",fg="blue")
lbtitle.grid(row=0,column=0)
mbtframe=Frame(win,height=400,width=1350,bd=10,relief="groove")
mbtframe.pack(side=BOTTOM)
F1frame=Frame(mbtframe,height=400,width=450,bd=10,relief="groove")
F1frame.pack(side=LEFT)
F2frame=Frame(mbtframe,height=400,width=450,bd=10,relief="groove")
F2frame.pack(side=LEFT)
F3frame=Frame(mbtframe,height=400,width=450,bd=10,relief="groove")
F3frame.pack(side=RIGHT)
# ---------------------------------All --chechbutton variable--------------
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()

#------------------ ------text variable for entry field Frame 1----------------
Evr1=StringVar()
Evr2=StringVar()
Evr3=StringVar()
Evr4=StringVar()
Evr5=StringVar()
Evr6=StringVar()
Evr7=StringVar()
Evr8=StringVar()
Evr9=StringVar()

# -----------------------text variable for entry field Frame 2-------------------
Evrf1=StringVar()
Evrf2=StringVar()
Evrf3=StringVar()
Evrf4=StringVar()
Evrf5=StringVar()
Evrf6=StringVar()
Evrf7=StringVar()
Evrf8=StringVar()
Evrf9=StringVar()

# -----------------------text variable for entry field Frame 2-------------------

Evrff3=StringVar()

# ------------------set all Checkbutton / Entry to 0------------------
Evr1.set('0')
Evr2.set('0')
Evr3.set('0')
Evr4.set('0')
Evr5.set('0')
Evr6.set('0')
Evr7.set('0')
Evr8.set('0')
Evr9.set('0')

Evrf1.set('0')
Evrf2.set('0')
Evrf3.set('0')
Evrf4.set('0')
Evrf5.set('0')
Evrf6.set('0')
Evrf7.set('0')
Evrf8.set('0')
Evrf9.set('0')


Evrff3.set('0')



var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)

# *****************************************************   CODING  ************
def quit():
    ppc=messagebox.askyesno("HELLO LOKESH",'ARE YOU SURE WANT TO EXIT')
    if ppc>0:
        win.destroy()
# -----------------------quit----------------

def rest():

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)

    Evr1.set('0')
    Evr2.set('0')
    Evr3.set('0')
    Evr4.set('0')
    Evr5.set('0')
    Evr6.set('0')
    Evr7.set('0')
    Evr8.set('0')
    Evr9.set('0')
    Evrf1.set('0')
    Evrf2.set('0')
    Evrf3.set('0')
    Evrf4.set('0')
    Evrf5.set('0')
    Evrf6.set('0')
    Evrf7.set('0')
    Evrf8.set('0')
    Evrf9.set('0')
    Evrff3.set('0')
    E1.config(state=DISABLED)
    E2.config(state=DISABLED)
    E3.config(state=DISABLED)
    E3.config(state=DISABLED)
    E4.config(state=DISABLED)
    E5.config(state=DISABLED)
    E6.config(state=DISABLED)
    E7.config(state=DISABLED)
    E8.config(state=DISABLED)
    E9.config(state=DISABLED)
    E10.config(state=DISABLED)
    E11.config(state=DISABLED)
    E12.config(state=DISABLED)
    E13.config(state=DISABLED)
    E14.config(state=DISABLED)
    E15.config(state=DISABLED)
    E16.config(state=DISABLED)
    E17.config(state=DISABLED)
    E18.config(state=DISABLED)
    E19.config(state=DISABLED)

# ----------------------------reset----------------
def tl():
    a=int(Evr1.get())
    b=int(Evr2.get())
    c=int(Evr3.get())
    d=int(Evr4.get())
    e=int(Evr5.get())
    f=int(Evr6.get())
    g=int(Evr7.get())
    h=int(Evr8.get())
    i=int(Evr9.get())
    j=int(Evrf1.get())
    k=int(Evrf2.get())
    l=int(Evrf3.get())
    m=int(Evrf4.get())
    n=int(Evrf5.get())
    o=int(Evrf6.get())
    p=int(Evrf7.get())
    q=int(Evrf8.get())
    r=int(Evrf9.get())
    outtotal=(a*30+b*40+c*40+d*50+e*50+f*40+g*40+h*60+i*20+j*10+k*50+l*90+m*60+n*70+o*60+p*50+q*30+r*90)
    Evrff3.set(outtotal)

# -----------------------------------------total-----------------
def Regular_veg():
    if var1.get() == 1:
        E1.config(state=NORMAL)
        Evr1.set("")
    elif  var1.get() == 0:
        E1.config(state=DISABLED)
        Evr1.set("0")

def jain_franky():
    if var2.get() == 1:
        E2.config(state=NORMAL)
        Evr2.set("")
    elif  var2.get() == 0:
        E2.config(state=DISABLED)
        Evr2.set("0")

def tawa_paneer():
    if var3.get() == 1:
        E3.config(state=NORMAL)
        Evr3.set("")
    elif  var3.get() == 0:
        E3.config(state=DISABLED)
        Evr3.set("0")
def chilly_paneer():
    if var4.get() == 1:
        E4.config(state=NORMAL)
        Evr4.set("")
    elif  var4.get() == 0:
        E4.config(state=DISABLED)
        Evr4.set("0")

def paneer_tandoori_tdka():
    if var5.get() == 1:
        E5.config(state=NORMAL)
        Evr5.set("")
    elif  var5.get() == 0:
        E5.config(state=DISABLED)
        Evr5.set("0")

def regular_chicken():
    if var6.get() == 1:
        E6.config(state=NORMAL)
        Evr6.set("")
    elif  var6.get() == 0:
        E6.config(state=DISABLED)
        Evr6.set("0")

def chicken_tikka():
    if var7.get() == 1:
        E7.config(state=NORMAL)
        Evr7.set("")
    elif  var7.get() == 0:
        E7.config(state=DISABLED)
        Evr7.set("0")

def chicken_manchurian():
    if var8.get() == 1:
        E8.config(state=NORMAL)
        Evr8.set("")
    elif  var8.get() == 0:
        E8.config(state=DISABLED)
        Evr8.set("0")

def chicken_tandoori_tdka():
    if var9.get() == 1:
        E9.config(state=NORMAL)
        Evr9.set("")
    elif  var9.get() == 0:
        E9.config(state=DISABLED)
        Evr9.set("0")

def c_ola():
    if var10.get() == 1:
        E10.config(state=NORMAL)
        Evrf1.set("")
    elif  var10.get() == 0:
        E10.config(state=DISABLED)
        Evrf1.set("0")
def t_ango():
    if var11.get() == 1:
        E11.config(state=NORMAL)
        Evrf2.set("")
    elif  var11.get() == 0:
        E11.config(state=DISABLED)
        Evrf2.set("0")
def root_beer():
    if var12.get() == 1:
        E12.config(state=NORMAL)
        Evrf3.set("")
    elif  var2.get() == 0:
        E12.config(state=DISABLED)
        Evrf3.set("0")
def S_quash():
    if var13.get() == 1:
        E13.config(state=NORMAL)
        Evrf4.set("")
    elif  var13.get() == 0:
        E13.config(state=DISABLED)
        Evrf4.set("0")
def Cream_soda():
    if var14.get() == 1:
        E14.config(state=NORMAL)
        Evrf5.set("")
    elif  var14.get() == 0:
        E14.config(state=DISABLED)
        Evrf5.set("0")
def lime_fresh():
    if var15.get() == 1:
        E15.config(state=NORMAL)
        Evrf6.set("")
    elif  var15.get() == 0:
        E15.config(state=DISABLED)
        Evrf6.set("0")
def san_grita():
    if var16.get() == 1:
        E16.config(state=NORMAL)
        Evrf7.set("")
    elif  var16.get() == 0:
        E16.config(state=DISABLED)
        Evrf7.set("0")
def ice_cream():
    if var17.get() == 1:
        E17.config(state=NORMAL)
        Evrf8.set("")
    elif  var17.get() == 0:
        E17.config(state=DISABLED)
        Evrf8.set("0")
def s_olo():
    if var18.get() == 1:
        E18.config(state=NORMAL)
        Evrf9.set("")
    elif  var18.get() == 0:
        E18.config(state=DISABLED)
        Evrf9.set("0")






# *****************************************************   CODING  ************

# ----------------------------Checkbutton-For frame 1 --------
lbtitle=Label(F1frame,font=("arial",50,'italic'),text="V & N Franky "+"   ")
lbtitle.grid(row=0,column=0)
Chk1=Checkbutton(F1frame,variable=var1,text="Regular Veg \t\t RS-30/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=Regular_veg)
Chk1.grid(row=1,column=0,sticky=W)
Chk2=Checkbutton(F1frame,variable=var2,text="Jain franky\t\t RS-40/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=jain_franky)
Chk2.grid(row=2,column=0,sticky=W)
Chk3=Checkbutton(F1frame,variable=var3,text="Tawa Paneer\t\t RS-40/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=tawa_paneer)
Chk3.grid(row=3,column=0,sticky=W)
Chk4=Checkbutton(F1frame,variable=var4,text="Chilly Paneer\t\t RS-50/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=chilly_paneer)
Chk4.grid(row=4,column=0,sticky=W)
Chk5=Checkbutton(F1frame,variable=var5,text="Paneer Tandoori Tadka\t RS-50/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=paneer_tandoori_tdka)
Chk5.grid(row=5,column=0,sticky=W)
Chk6=Checkbutton(F1frame,variable=var6,text="Regular Chicken\t\t RS-40/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=regular_chicken)
Chk6.grid(row=6,column=0,sticky=W)
Chk7=Checkbutton(F1frame,variable=var7,text="Chicken Tikka\t\t RS-40/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=chicken_tikka)
Chk7.grid(row=7,column=0,sticky=W)
Chk8=Checkbutton(F1frame,variable=var8,text="Chicken Manchurian\t RS-60/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=chicken_manchurian)
Chk8.grid(row=8,column=0,sticky=W)
Chk9=Checkbutton(F1frame,variable=var9,text="Chicken Tandoori Tadka\t RS-20/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=chicken_tandoori_tdka)
Chk9.grid(row=9,column=0,sticky=W)
lspace=Label(F1frame,text="\n\n").grid(row=11,column=0)

# --------------------------------Checkbutton- for-Frame 2------------------------------------------

lbtitle=Label(F2frame,font=("arial",50,'italic'),text="Soft Drink"+"  ")
lbtitle.grid(row=0,column=0)
Chk1=Checkbutton(F2frame,variable=var10,text="Cola\t\t RS-10/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=c_ola)
Chk1.grid(row=1,column=0)
Chk2=Checkbutton(F2frame,variable=var11,text="Tango\t\t RS-50/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=t_ango)
Chk2.grid(row=2,column=0,sticky=W)
Chk3=Checkbutton(F2frame,variable=var12,text="Root Bear\t RS-90/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=root_beer)
Chk3.grid(row=3,column=0,sticky=W)
Chk4=Checkbutton(F2frame,variable=var13,text="Squash\t\t RS-60/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=S_quash)
Chk4.grid(row=4,column=0,sticky=W)
Chk5=Checkbutton(F2frame,variable=var14,text="Cream soda\t RS-70/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=Cream_soda)
Chk5.grid(row=5,column=0,sticky=W)
Chk6=Checkbutton(F2frame,variable=var15,text="lime fresh\t RS-60/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=lime_fresh)
Chk6.grid(row=6,column=0,sticky=W)
Chk7=Checkbutton(F2frame,variable=var16,text="Sangrita\t\t RS-50/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=san_grita)
Chk7.grid(row=7,column=0,sticky=W)
Chk8=Checkbutton(F2frame,variable=var17,text="Ice Cream Folat\t RS-30/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=ice_cream)
Chk8.grid(row=8,column=0,sticky=W)
Chk9=Checkbutton(F2frame,variable=var18,text="Solo\t\t RS-90/Qty",font=('arial',18,'bold'),fg='#4a211d',onvalue=1,offvalue=0,command=s_olo)
Chk9.grid(row=9,column=0,sticky=W)
lspace=Label(F2frame,text="\    \n").grid(row=11,column=0)

# -----------------------------Entry Field for Frame 1----------------------------------

E1=Entry(F1frame,textvariable=Evr1,font=("arial",15,'bold'),state="disabled",width=7)
E1.grid(row=1,column=1)
E2=Entry(F1frame,textvariable=Evr2,font=("arial",15,'bold'),state="disabled",width=7)
E2.grid(row=2,column=1)
E3=Entry(F1frame,textvariable=Evr3,font=("arial",15,'bold'),state="disabled",width=7)
E3.grid(row=3,column=1)
E4=Entry(F1frame,textvariable=Evr4,font=("arial",15,'bold'),state="disabled",width=7)
E4.grid(row=4,column=1)
E5=Entry(F1frame,textvariable=Evr5,font=("arial",15,'bold'),state="disabled",width=7)
E5.grid(row=5,column=1)
E6=Entry(F1frame,textvariable=Evr6,font=("arial",15,'bold'),state="disabled",width=7)
E6.grid(row=6,column=1)
E7=Entry(F1frame,textvariable=Evr7,font=("arial",15,'bold'),state="disabled",width=7)
E7.grid(row=7,column=1)
E8=Entry(F1frame,textvariable=Evr8,font=("arial",15,'bold'),state="disabled",width=7)
E8.grid(row=8,column=1)
E9=Entry(F1frame,textvariable=Evr9,font=("arial",15,'bold'),state="disabled",width=7)
E9.grid(row=9,column=1)
# -------------------------------------------Entry for frame 2-----------------

E10=Entry(F2frame,textvariable=Evrf1,font=("arial",15,'bold'),state="disabled",width=7)
E10.grid(row=1,column=1)
E11=Entry(F2frame,textvariable=Evrf2,font=("arial",15,'bold'),state="disabled",width=7)
E11.grid(row=2,column=1)
E12=Entry(F2frame,textvariable=Evrf3,font=("arial",15,'bold'),state="disabled",width=7)
E12.grid(row=3,column=1)
E13=Entry(F2frame,textvariable=Evrf4,font=("arial",15,'bold'),state="disabled",width=7)
E13.grid(row=4,column=1)
E14=Entry(F2frame,textvariable=Evrf5,font=("arial",15,'bold'),state="disabled",width=7)
E14.grid(row=5,column=1)
E15=Entry(F2frame,textvariable=Evrf6,font=("arial",15,'bold'),state="disabled",width=7)
E15.grid(row=6,column=1)
E16=Entry(F2frame,textvariable=Evrf7,font=("arial",15,'bold'),state="disabled",width=7)
E16.grid(row=7,column=1)
E17=Entry(F2frame,textvariable=Evrf8,font=("arial",15,'bold'),state="disabled",width=7)
E17.grid(row=8,column=1)
E18=Entry(F2frame,textvariable=Evrf9,font=("arial",15,'bold'),state="disabled",width=7)
E18.grid(row=9,column=1)
# -------------------Entry field for frame 3-------------------------------
E19=Entry(F3frame,fg='blue',width=7,state=DISABLED,font=('arial',16,'bold'),textvariable=Evrff3)
E19.grid(row=1,column=2)
# --------------------------------------------logic--Buttons for 3rd frame---------

lb=Label(F3frame,text="\n\n\n\n\n\n",font=('arial',16,'bold')).grid(row=0,column=0)

B1=Button(F3frame,text="TOTAL",padx=14,pady=1,bd=3,bg="green",font=('arial',10,'bold'),width=4,command=tl)
B1.grid(row=2,column=2)
B2=Button(F3frame,text="RESET",command=rest,padx=14,pady=1,bd=3,bg="#4287f5",font=('arial',10,'bold'),width=4)
B2.grid(row=3,column=1)
B3=Button(F3frame,text="EXIT",command=quit,padx=10,bg="#f57242",pady=1,bd=3,font=('arial',10,'bold'),width=4)
B3.grid(row=3,column=3)
lbs=Label(F3frame,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n").grid(row=4,column=0)
win.mainloop()
