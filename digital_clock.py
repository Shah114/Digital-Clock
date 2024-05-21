# Modules
from tkinter import Tk
from tkinter import Label
import time

master = Tk()
master.title("Digital Clock")

# Functions
def get_time():
    '''This function is getting time for us.'''
    time_var = time.strftime("%I:%M:%S %p")
    clock.config(text=time_var)
    clock.after(200, get_time)

# Main part
clock = Label(master, font=('Calibri', 90), bg='grey', fg='white')
clock.pack()

get_time()

master.mainloop()