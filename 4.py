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
