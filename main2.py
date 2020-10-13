from tkinter import*

window=Tk()
window.geometry("300x300")
window.title("Temperature")

inputNum= StringVar()
l1=Label(window,text="Celsius To Fahrenheit")
l1.place(x=110, y=50)
e1=Entry(window, bd=3)
e1.place(x=110,y=150)

l2=Label(window,text="Fahrenheit to Celsius")
l2.place(x=500, y= 50)
e2=Entry(window,bd=3)
e2.place(x=500,y=150)

button1=Button(window, text="Activate-Celsius to Fahrenheit")
button1.place(x=110,y=250)

button2=Button(window, text="Activate-Fahrenheit to Celsius")
button2.place(x=500, y=250)

def clear_all():
    e1.delete(0,END)
    e2.delete(0,END)
btnc=Button(window, text="Clear", command=clear_all)
btnc.place(x=600,y=350)

def exit_all():
    window.destroy()
btne=Button(window,text="Exit Program", command= exit_all)
btne.place(x=600,y=400)

def celtofah():
    f=float('Celsius', "Please enter the temperature in celsius: ")
    f=input("") * 9/5 + 32




btn3=Button(window,text="Calculate Conversion")
btn3.place(x=110,y=350)




window.mainloop()
