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