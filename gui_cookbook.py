#Nötige Imports
import tkinter as tk
from tkinter import ttk

#Erzeugen eines Fensters
win = tk.Tk()

#Titel des Fensters
win.title("Python GUI")

#Label 
a_label = ttk.Label(win, text= "Enter a Name:")
a_label.grid(column =0, row=0)

#2tes Label
ttk.Label(win, text="Choose a Number: ").grid(column=1, row=0)
number = tk.StringVar()

#Textbox
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column= 0, row=1)

#Button (param: disabled)
action=ttk.Button(win,text= "Click Me!", command=click_me)
action.grid(column =2, row =1)
#action.config(state='disabled') #Disablen eines Buttons

#Event-Funktion für den Button
def click_me():
	action.configure(text="Hello " + name.get() + ' ' + number.get())

#Combobox (param:Read-only + Focus auf Eingabe)
number_chosen= ttk.Combobox(win, width=12, textvariable= number, state='readonly')
number_chosen['values'] = (1,2,42,100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

name_entered.focus() #Focus auf das Name Feld mit Eingabe

#=================
#Start der GUI
win.mainloop()
#=================
