#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x500")

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text="Contains", width=20, command=display_text).pack(pady=5)
ttk.Button(win, text="Contains at Index", width=20, command=display_text).pack(pady=5)
ttk.Button(win, text="Doesn't Contain", width=20, command=display_text).pack(pady=5)
ttk.Button(win, text="Doesn't Contains at index", width=20, command=display_text).pack(pady=5)
ttk.Button(win, text="Remove Word", width=20, command=display_text).pack(pady=5)

win.mainloop()