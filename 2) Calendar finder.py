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

