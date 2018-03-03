#import Tkinter as tk
import tkinter as tk
from tkinter import ttk
#from Tkinter import ttk

#Create an Instance
win = tk.Tk()

#Add a title
win.title("Python GUI")

#Adding a Label that will get modified
a_label = ttk.Label(win, text= "Enter a Name:")
a_label.grid(column =0, row=0)

#Button Click event function
def click_me():
	action.configure(text="Hello " + name.get() + ' ' + number.get())

#Adding a Textbox
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column= 0, row=1)

#Adding a Button
action=ttk.Button(win,text= "Click Me!", command=click_me)
action.grid(column =2, row =1)
#action.config(state='disabled') #Disablen eines Buttons

ttk.Label(win, text="Choose a Number: ").grid(column=1, row=0)
number = tk.StringVar()

#Read-only Combobox
number_chosen= ttk.Combobox(win, width=12, textvariable= number, state='readonly')
number_chosen['values'] = (1,2,42,100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

name_entered.focus() #Focus auf das Name Feld mit Eingabe

#=================
#Start GUI
win.mainloop()
#=================
