from tkinter import*

window=Tk()
window.geometry("700x500")
window.title("Converting Temperature")

result1 = IntVar()
result2 = IntVar()

lft_frame = LabelFrame(window, text="Celcius To Fahrenheit",bg="red")
rgt_frame = LabelFrame(window, text="Fahrenheit To Celcius", bg="red")
lft_frame.pack(fill="both", expand="yes", side="left")
rgt_frame.pack(fill="both", expand="yes", side="right")

e1 = Entry(lft_frame,textvariable= result1, state="disable")
e1.place(x=50,y=150)

e2 = Entry(rgt_frame,textvariable= result2, state= "disable")
e2.place(x=50,y=150)

btn_frame = LabelFrame(window, text="Test")
btn_frame.pack(fill="both", expand="yes", side="bottom")

def celcius_acive():
    e1.configure(state="normal")
button1=Button(lft_frame, text="Activate-Celcius to Fahrenheit",command= celcius_acive)
button1.place(x=50,y=200)

def fah_active():
    e2.configure(state="normal")
button2=Button(rgt_frame, text="Activate-Fahrenheit to Celcius",command= fah_active)
button2.place(x=50, y=200)


def exit_all():
    window.destroy()

btne = Button(rgt_frame,text="Exit Program", command= exit_all)
btne.place(x=150,y=400)

#converting celsius to fahrenheit
def convert2fah():
    if e1:
        celcius= float(e1.get())
        fah= (celcius * 9/5) + 32
        answers.insert(0, fah)

answers = Entry(window,bg="light green")
answers.place(x= 250, y=250)

#converting from fahrenheit to celsius
def convert2cel():
        if  e2:
            fah=float(e2.get())
            celcius= (fah- 32) * 5/9
            answers.insert(0, celcius)

btn3=Button(lft_frame,text="Calculate Conversion to fah",command= convert2fah)
btn3.place(x=50,y=300)
btn4=Button(lft_frame,text="Calculate Conversion to cel",command= convert2cel)
btn4.place(x=50,y=400)

def clear_all():
    e1.delete(0,END)
    e2.delete(0,END)
    answers.delete(0, END)

btnc = Button(rgt_frame, text="Clear", command=clear_all)
btnc.place(x=200,y=300)


window.mainloop()







