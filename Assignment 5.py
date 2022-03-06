# ASSIGNMENT 5

#_________________________Question 1_________________________

from tkinter import *

# Calculate GST
def GST():
    # Taking input
    oc=int(original_enter.get())
    np=int(net_enter.get())
    # Calculating Gst 
    c=(((np-oc)*100)/oc)
    Gst.insert(10, str(c)+'%')

# Clearing the input and output widgets
def clear():
    original_enter.delete(0, END)
    net_enter.delete(0, END)
    Gst.delete(0, END)

# Creating window to take inputs and display outputs
Gst_calculator=Tk()
Gst_calculator.title('GST Calculator')
original_cost=Label(Gst_calculator, text='Enter original cost')
original_cost.grid(row=0,column=0)
original_enter=Entry(Gst_calculator)
original_enter.grid(row=0,column=1)

net_price=Label(Gst_calculator, text='Enter net price')
net_price.grid(row=1,column=0)
net_enter=Entry(Gst_calculator)
net_enter.grid(row=1,column=1)


calculate_btn=Button(Gst_calculator, text='Calculate GST', command=GST)
calculate_btn.grid(row=2,column=1)

Gst=Entry(Gst_calculator)
Gst.grid(row=4,column=1)

clearit=Button(Gst_calculator, text='Clear', command=clear)
clearit.grid(row=5,column=1)

# Start window
Gst_calculator.mainloop()

#_________________________Question 2_________________________

import calendar
from tkinter import *

# Function to find required calendar
def Calendar():
    # Creating window for output
    showcal=Tk()
    showcal.title('Calendar')

    # taking input
    get_year=int(year_inp.get())

    # Calendar output
    cal_content=calendar.calendar(get_year)
    cal_label=Label(showcal, text=cal_content)
    cal_label.grid(row=0,column=4)

    # Starting window for output
    showcal.mainloop()

# WIndow for taking inputs
cal=Tk()
cal.title('Calendar Finder')

year=Label(cal, text='Enter year')
year.grid(row=0,column=0)

year_inp=Entry(cal)
year_inp.grid(row=0,column=1)

calendar_btn=Button(cal, text='Get Calendar', command=Calendar, pady=10)
calendar_btn.grid(row=1,column=1)

# Starting window
cal.mainloop()

#_________________________Question 3_________________________

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

#___________________________Question 4_________________________

from tkinter import *

# Creating list for marks
marks_list=list()

# Function to create list from individual inputs
def marks():
    global marks_list
    num=int(marks_inp.get())

    # Append all individual elements into list
    marks_list.append(num)

    # Entering in label and removing redundant elements
    mark_list_entry.config(text=(marks_list))
    marks_inp.delete(0,END)
    marks_sort_list.config(text='')

# Function to quick sort
sequence=[]
def quick_sort(sequence):
    length=len(sequence)

    # For one element list
    if length<=1:
        return sequence

    # Creating pivot
    else:
        pivot=sequence.pop()

    # Creating two different lists around pivot
    items_greater=[]
    items_lower=[]

    # Entering elements into the two lists
    for item in sequence:
        if item>pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    # Using recursion for the two separate lists
    return quick_sort(items_lower)+[pivot]+quick_sort(items_greater)

# Function to implement quick sort
def marks_sort():
    global marks_list
    sequence=marks_list
    sorted_marks_list=quick_sort(sequence)

    # Entering in label and removing redundant elements
    marks_sort_list.config(text=str(sorted_marks_list))
    mark_list_entry.config(text='')

# Function to clear all input or output widgets
def clearit():
    global marks_list
    marks_list=[]
    marks_inp.delete(0,END)
    mark_list_entry.config(text='')
    marks_sort_list.config(text='')


marks_var=StringVar    

# Creating the window and its widgets
Marks_sorted_list=Tk()
Marks_sorted_list.title('List of marks')
marks_lbl=Label(Marks_sorted_list, text='Enter individual marks of student')
marks_lbl.grid(row=0,column=0)

marks_inp=Entry(Marks_sorted_list, textvariable=marks_var)
marks_inp.grid(row=0,column=1)

Enter=Button(Marks_sorted_list, text='Enter', command=marks)
Enter.grid(row=1,column=1)

mark_list_lbl=Label(Marks_sorted_list, text='Marks List')
mark_list_lbl.grid(row=2,column=0)

mark_list_entry=Label(Marks_sorted_list)
mark_list_entry.grid(row=2,column=1)

marks_sort_btn=Button(Marks_sorted_list, text='Sort List', command=marks_sort)
marks_sort_btn.grid(row=3,column=1)

marks_sort_lbl=Label(Marks_sorted_list, text='Sorted List')
marks_sort_lbl.grid(row=4,column=0)

marks_sort_list=Label(Marks_sorted_list, text='')
marks_sort_list.grid(row=4,column=1)

clear_btn=Button(Marks_sorted_list, text='Clear', command=clearit)
clear_btn.grid(row=5 ,column=1)

# Code to start window
Marks_sorted_list.mainloop()


#_________________________Question 5_________________________

from tkinter import *

# Creating function to take individual inputs to make array
array=list()
def makearray():
    global array

    # Taking inputs
    num=int(num_inp.get())

    # Appending inputs to array
    array.append(num)

    # Creating array and removing redundant output
    created_arr.config(text=(array))
    num_inp.delete(0,END)
    sorted_arr.config(text='')

# Fuction to sort array
def sort_array():
    global array
    # Sorting array
    array.sort()
    # Output of result
    sorted_arr.config(text=str(array))
    created_arr.config(text='')

# Function for binary search
def binary_search():
    global array
    search=int(search_inp.get())
    low=0
    high=len(array)-1
    mid=0
    while low<=high:
        mid=(high+low)//2

        if array[mid]<search:
            low=mid+1
        
        elif array[mid]>search:
            high=mid-1
        
        else:
            return mid
        
    return -1

# Function to implement binary search
def location():
    result=binary_search()

    # When element is not in array
    if result==-1:
        result_inp.config(text='Entry not present')

    # When element is in array
    else:
        result_inp.config(text=str(result))
    
    search_inp.delete(0,END)

# To count the number of occurences in array
def occurence():
    global array

    # Taking input
    num_occur=int(occur_inp.get())

    # Counting occurences
    occur_count=array.count(num_occur)

    # Output
    return occur_out_entry.config(text=str(occur_count))

# Function to clear all input and output widgets
def clearall():
    global array
    array=[]
    num_inp.delete(0,END)
    created_arr.config(text='')
    sorted_arr.config(text='')
    search_inp.delete(0,END)
    result_inp.config(text='')
    occur_inp.delete(0,END)
    occur_out_entry.config(text='')

# Creating window for taking inputs and displaying outputs
win=Tk()
win.title('Sorting, searching and counting in array')

num_lbl=Label(win, text='Enter numbers to form array')
num_lbl.grid(row=0,column=0)

num_inp=Entry(win)
num_inp.grid(row=0,column=1)

create_btn=Button(win, text='Enter individual elements to Array',
command=makearray)
create_btn.grid(row=1, column=1)

ur_ar=Label(win, text='Your array: ')
ur_ar.grid(row=2,column=0)

created_arr=Label(win, text='')
created_arr.grid(row=2,column=1)

sort_arr=Button(win, text='Sort Array', command=sort_array)
sort_arr.grid(row=3,column=1)

sort_arr_lbl=Label(win, text='Sorted Array')
sort_arr_lbl.grid(row=4,column=0)

sorted_arr=Label(win, text='')
sorted_arr.grid(row=4,column=1)

search_lbl=Label(win, text='Enter the element to search')
search_lbl.grid(row=5,column=0)

search_inp=Entry(win)
search_inp.grid(row=5,column=1)

search_btn=Button(win, text='Search', command=location)
search_btn.grid(row=6,column=1)

result_lbl=Label(win, text="Location of element")
result_lbl.grid(row=7,column=0)

result_inp=Label(win, text='')
result_inp.grid(row=7,column=1)

occur_lbl=Label(win, text='Check occurences of elements')
occur_lbl.grid(row=8,column=0)

occur_inp=Entry(win)
occur_inp.grid(row=8,column=1)

occur_btn=Button(win, text='Check occurences', command=occurence)
occur_btn.grid(row=9,column=1)

occur_out_lbl=Label(win, text='Number of occurences')
occur_out_lbl.grid(row=10,column=0)

occur_out_entry=Label(win, text='')
occur_out_entry.grid(row=10,column=1)

clear_btn=Button(win, text='Clear', command=clearall)
clear_btn.grid(row=11,column=1)

# Starting the window
win.mainloop()

#__________________________OVER__________________________
