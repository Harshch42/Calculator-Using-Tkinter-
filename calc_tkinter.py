import tkinter as tk
from tkinter import *

root = tk.Tk()

expression = ""

def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)

def equalpress():
    try:
        global expression

        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")





root.geometry('600x700')
root.resizable(False,False)


root.title('Calculator')

equation = StringVar()

text_field = Entry(root,width = 600,bg = '#fff',background = "light Blue",font = ('Times New Roman',55), textvariable=equation).place(x = 0,y = 100 )

b20 = Button(root, text = "Calculator",background = "pink",pady=10,font=('Times New Roman',50, 'bold'))
b20.place(width =400,height = 80,x = 100 , y = 10)


b10 = Button(root, text = "C",activeforeground = "Blue",activebackground = "pink",command=clear,pady=10,font=('Times New Roman', 25, 'bold'))
b10.place(width =300,height = 100,x = 0 , y = 200)

b12 = Button(root, text = "%",activeforeground = "Blue",activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
b12.place(width =150,height = 100,x = 300 , y = 200)


b7 = Button(root, text = "7",activeforeground = "Blue",activebackground = "pink",command=lambda: press(7),pady=10,font=('Times New Roman', 25, 'bold'))
b7.place(width =150,height = 100,x = 0 , y = 300)

b8 = Button(root, text = "8",activeforeground = "Blue",activebackground = "pink",command=lambda: press(8),pady=10,font=('Times New Roman', 25, 'bold'))
b8.place(width =150,height = 100,x = 150 , y = 300)

b9 = Button(root, text = "9",activeforeground = "Blue",activebackground = "pink",command=lambda: press(9),pady=10,font=('Times New Roman', 25, 'bold'))
b9.place(width =150,height = 100,x = 300 , y = 300)

b4 = Button(root, text = "4",activeforeground = "Blue",activebackground = "pink",command=lambda: press(4),pady=10,font=('Times New Roman', 25, 'bold'))
b4.place(width =150,height = 100,x = 0 , y = 400)

b5 = Button(root, text = "5",activeforeground = "Blue",activebackground = "pink",command=lambda: press(5),pady=10,font=('Times New Roman', 25, 'bold'))
b5.place(width =150,height = 100,x = 150 , y = 400)

b6 = Button(root, text = "6",activeforeground = "Blue",activebackground = "pink",command=lambda: press(6),pady=10,font=('Times New Roman', 25, 'bold'))
b6.place(width =150,height = 100,x = 300 , y = 400)

b1 = Button(root, text = "1",activeforeground = "Blue",activebackground = "pink",command=lambda: press(1),pady=10,font=('Times New Roman', 25, 'bold'))
b1.place(width =150,height = 100,x = 0 , y = 500)

b2 = Button(root, text = "2",activeforeground = "Blue",activebackground = "pink",command=lambda: press(2),pady=10,font=('Times New Roman', 25, 'bold'))
b2.place(width =150,height = 100,x = 150 , y = 500)

b3 = Button(root, text = "3",activeforeground = "Blue",activebackground = "pink",command=lambda: press(3),pady=10,font=('Times New Roman', 25, 'bold'))
b3.place(width =150,height = 100,x = 300 , y = 500)

b13 = Button(root, text = "del",activeforeground = "Blue",activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
b13.place(width =150,height = 100,x = 0 , y = 600)

b0 = Button(root, text = "0",activeforeground = "Blue",activebackground = "pink",command=lambda: press(0),pady=10,font=('Times New Roman', 25, 'bold'))
b0.place(width =150,height = 100,x = 150 , y = 600)

b14 = Button(root, text = ".",activeforeground = "Blue",activebackground = "pink",command=lambda: press('.'),pady=10,font=('Times New Roman', 25, 'bold'))
b14.place(width =150,height = 100,x = 300 , y = 600)


b15 = Button(root, text = "/",activeforeground = "Blue",activebackground = "pink",command=lambda: press("/"),pady=10,font=('Times New Roman', 25, 'bold'))
b15.place(width =150,height = 100,x = 450 , y = 200)

b16 = Button(root, text = "*",activeforeground = "Blue",activebackground = "pink",command=lambda: press("*"),pady=10,font=('Times New Roman', 25, 'bold'))
b16.place(width =150,height = 100,x = 450 , y = 300)

b17 = Button(root, text = "-",activeforeground = "Blue",activebackground = "pink",command=lambda: press("-"),pady=10,font=('Times New Roman', 25, 'bold'))
b17.place(width =150,height = 100,x = 450 , y = 400)

b18 = Button(root, text = "+",activeforeground = "Blue",activebackground = "pink",command=lambda: press("+"),pady=10,font=('Times New Roman', 25, 'bold'))
b18.place(width =150,height = 100,x = 450 , y = 500)

b19 = Button(root, text = "=",activeforeground = "Blue",activebackground = "pink",command=equalpress,pady=10,font=('Times New Roman', 25, 'bold'))
b19.place(width =150,height = 100,x = 450 , y = 600)




root.mainloop()
