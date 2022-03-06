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