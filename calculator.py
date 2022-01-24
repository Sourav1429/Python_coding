import tkinter
from tkinter import *
root=Tk()
root.geometry("500x200");
d=0;
op=-1;
arg1=-1;
#mm
#
#designing
def but_0():
#my_label=Label(e,text=str(10*float(e.get())))
#my_label.pack()
    global d;
    d=e.get()
    e.delete(0,END)
    e.insert(0,str(10*float(d)))
    return
def but_00():
    e.delete(0,END)
    e.insert(0,"0")
    return
def but_1():
#my_label=Label(e,text=str(10*float(e.get())+1))
#my_label.pack()
    global d;
    d=e.get()
    e.delete(0,END)
    e.insert(0,str(10*float(d)+1))
    return
def but_2():
#my_label=Label(e,text=str(10*float(e.get())+2))
#my_label.pack()
    global d;
    d=e.get()
    e.delete(0,END)
    e.insert(0,str(10*float(d)+2))
    return
def but_3():
#my_label=Label(e,text=str(10*float(e.get())+3))
#my_label.pack()
    global d;
    d=e.get()
    e.delete(0,END)
    e.insert(0,str(10*float(d)+3))
    return
def but_4():
#my_label=Label(e,text=str(10*float(e.get())+4))
#my_label.pack()
    global d;
    d=e.get()
    e.delete(0,END)
    e.insert(0,str(10*float(d)+4))
    return
def but_5():
#my_label=Label(e,text=str(10*float(e.get())+5))
#my_label.pack()
    global d;
    d=e.get()
    e.delete(0,END)
    e.insert(0,str(10*float(d)+5))
    return
def but_6():
#my_label=Label(e,text=str(10*float(e.get())+6))
#my_label.pack()
    global d;
    d=e.get()
    e.delete(0,END)
    e.insert(0,str(10*float(d)+6))
    return
def but_7():
#my_label=Label(e,text=str(10*float(e.get())+7))
#my_label.pack()
    global d;
    d=e.get()
    e.delete(0,END)
    e.insert(0,str(10*float(d)+7))
    return
def but_8():
#my_label=Label(e,text=str(10*float(e.get())+8))
#my_label.pack()
    global d;
    d=e.get()
    e.delete(0,END)
    e.insert(0,str(10*float(d)+8))
    return
def but_9():
#my_label=Label(e,text=str(10*float(e.get())+9))
#my_label.pack()
    global d;
    d=e.get()
    e.delete(0,END)
    e.insert(0,str(10*float(d)+9))
    return

def sum1():
    global arg1
    global op;
    arg1=float(e.get())
    e.delete(0,END)
    e.insert(0,0)
    op=0;
    return
def equal():
    global arg1
    global op
    if(op==0):
        arg1=arg1+float(e.get())
    elif(op==1):
        arg1=arg1-float(e.get())
    elif(op==2):
        arg1=arg1*float(e.get())
    elif(op==3):
        arg1=arg1/float(e.get())
    e.delete(0,END)
    e.insert(0,str(arg1))
    return
def diff():
    global arg1
    global op
    arg1=float(e.get())
    e.delete(0,END)
    e.insert(0,0)
    op=1;
    return
def mul():
    global arg1
    global op
    arg1=float(e.get())
    e.delete(0,END)
    e.insert(0,0)
    op=2;
    return
def div():
    global arg1
    global op
    arg1=float(e.get())
    e.delete(0,END)
    e.insert(0,0)
    op=3;
    return
#
#defining
button_0=Button(root,text="0",padx=50,pady=20,command=but_0)
button_00=Button(root,text="C",padx=50,pady=20,command=but_00)
button_1=Button(root,text="1",padx=50,pady=10,command=but_1)
button_2=Button(root,text="2",padx=50,pady=10,command=but_2)
button_3=Button(root,text="3",padx=50,pady=10,command=but_3)
button_4=Button(root,text="4",padx=50,pady=10,command=but_4)
button_5=Button(root,text="5",padx=50,pady=10,command=but_5)
button_6=Button(root,text="6",padx=50,pady=10,command=but_6)
button_7=Button(root,text="7",padx=50,pady=10,command=but_7)
button_8=Button(root,text="8",padx=50,pady=10,command=but_8)
button_9=Button(root,text="9",padx=50,pady=10,command=but_9)
button_eq=Button(root,text="=",padx=50,pady=20,command=equal)
button_s=Button(root,text="+",padx=50,pady=20,command=sum1)
button_d=Button(root,text="-",padx=50,pady=10,command=diff)
button_m=Button(root,text="*",padx=50,pady=10,command=mul)
button_di=Button(root,text="/",padx=50,pady=10,command=div)
e=Entry(root,width=50,bg="WHITE",fg="BLACK",justify='right')
e.insert(0,0)
#

#placing
e.grid(row=0,column=0,columnspan=4)
button_7.grid(row=1,column=0,columnspan=1)
button_8.grid(row=1,column=1,columnspan=1)
button_9.grid(row=1,column=2,columnspan=1)
button_4.grid(row=2,column=0,columnspan=1)
button_5.grid(row=2,column=1,columnspan=1)
button_6.grid(row=2,column=2,columnspan=1)
button_1.grid(row=3,column=0,columnspan=1)
button_2.grid(row=3,column=1,columnspan=1)
button_3.grid(row=3,column=2,columnspan=1)
button_0.grid(row=4,column=0,columnspan=1)
button_00.grid(row=4,column=1,columnspan=1)
button_eq.grid(row=4,column=2,columnspan=1)
button_s.grid(row=4,column=3,rowspan=1)
button_d.grid(row=3,column=3,rowspan=1)
button_m.grid(row=2,column=3,rowspan=1)
button_di.grid(row=1,column=3,rowspan=1)
#
root.resizable(0,0)
root.mainloop()
