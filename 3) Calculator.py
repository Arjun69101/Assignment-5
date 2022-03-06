from tkinter import *

expression=''

# Taking inputs
def number(num):
    global expression
    # Adding on from buttons pressed
    expression=expression+str(num)
    equation.set(expression)
    
# Calculating the equation
def evaluation():
    # Equation is valid
    try:
        global expression
        solution=str(eval(expression))
        equation.set(solution)
        expression=''
    # Equation is invalid
    except:
        equation.set(" error ")
        expression = ""

# Clear the calculator
def clear():
    global expression
    expression = ""
    equation.set("")

# Creating window for inputs
calc=Tk()
calc.title('Calculator')

equation=StringVar()

number_entry=Entry(calc, textvariable=equation)
number_entry.grid(row=0,columnspan=3)

btn1=Button(calc, text='1', background='blue', foreground='white',height=1, width=6,
activebackground='red', activeforeground='black', command=lambda: number(1))
btn1.grid(row=1,column=0)

btn2=Button(calc, text='2', background='blue', foreground='white',height=1, width=6,
activebackground='red', activeforeground='black', command=lambda: number(2))
btn2.grid(row=1,column=1)

btn3=Button(calc, text='3', background='blue', foreground='white',height=1, width=6,
activebackground='red', activeforeground='black', command=lambda: number(3))
btn3.grid(row=1,column=2)

btn4=Button(calc, text='4', background='blue', foreground='white',height=1, width=6,
activebackground='red', activeforeground='black', command=lambda: number(4))
btn4.grid(row=2,column=0)

btn5=Button(calc, text='5', background='blue', foreground='white',height=1, width=6,
activebackground='red', activeforeground='black', command=lambda: number(5))
btn5.grid(row=2,column=1)

btn6=Button(calc, text='6', background='blue', foreground='white',height=1, width=6,
activebackground='red', activeforeground='black', command=lambda: number(6))
btn6.grid(row=2,column=2)

btn7=Button(calc, text='7', background='blue', foreground='white',height=1, width=6,
activebackground='red', activeforeground='black', command=lambda: number(7))
btn7.grid(row=3,column=0)

btn8=Button(calc, text='8', background='blue', foreground='white',height=1, width=6,
activebackground='red', activeforeground='black', command=lambda: number(8))
btn8.grid(row=3,column=1)

btn9=Button(calc, text='9', background='blue', foreground='white',height=1, width=6,
activebackground='red', activeforeground='black', command=lambda: number(9))
btn9.grid(row=3,column=2)

btn0=Button(calc, text='0', background='blue', foreground='white',height=1, width=6,
activebackground='red', activeforeground='black', command=lambda: number(0))
btn0.grid(row=4,column=0)

add_btn=Button(calc, text='+', background='blue', foreground='white',
activebackground='red', activeforeground='black', height=1, width=6,
command=lambda: number('+'))
add_btn.grid(row=1,column=4)

sub_btn=Button(calc, text='-', background='blue', foreground='white',
activebackground='red', activeforeground='black', height=1, width=6,
command=lambda: number('-'))
sub_btn.grid(row=2,column=4)

mult_btn=Button(calc, text='*', background='blue', foreground='white',
activebackground='red', activeforeground='black', height=1, width=6,
command=lambda: number('*'))
mult_btn.grid(row=3,column=4)

div_btn=Button(calc, text='/', background='blue', foreground='white',
activebackground='red', activeforeground='black', height=1, width=6,
command=lambda: number('/'))
div_btn.grid(row=4,column=4)

decimal_btn=Button(calc, text='.', background='blue', foreground='white',
activebackground='red', activeforeground='black', height=1, width=6,
command=lambda: number('.'))
decimal_btn.grid(row=4,column=1)

equal_btn=Button(calc, text='=', background='blue', foreground='white',
activebackground='red', activeforeground='black', height=1, width=6,
command= evaluation)
equal_btn.grid(row=4,column=2)

clear_btn=Button(calc, text='clear', background='blue', foreground='white',
activebackground='red', activeforeground='black',height=1, width=6 ,
command=clear)
clear_btn.grid(row=5,column=2)

# To start the window
calc.mainloop()
