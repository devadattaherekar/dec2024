import tkinter as tk

window=tk.Tk()
window.title("First UI Application")
window.geometry("800x600")
label1=tk.Label(text="Enter First Number",bg="yellow",width=30)
label1.place(x=20,y=60)
label2=tk.Label(text="Enter Second Number",bg="light blue",width=30)
label2.place(x=20,y=120)
label3=tk.Label(text="Result",bg="light pink",width=30)
label3.place(x=20,y=180)

var1=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()

textbox1=tk.Entry(textvariable=var1,width=30).place(x=300,y=60)
textbox2=tk.Entry(textvariable=var2,width=30).place(x=300,y=120)
textbox3=tk.Entry(textvariable=var3,width=30).place(x=300,y=180)

def calculate():
    var3.set(int(var1.get())+int(var2.get()))

def clear():
    var1.set("")
    var2.set("")
    var3.set("")

button1=tk.Button(text="SUM",width=30,background="yellow",command=calculate).place(x=600,y=60)
button2=tk.Button(text="CLEAR",width=30,background="light blue",command=clear).place(x=600,y=120)
button3=tk.Button(text="EXIT",width=30,background="light pink",command=window.destroy).place(x=600,y=180)


window.mainloop()
#print("hello world")
