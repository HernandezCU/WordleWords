#Import the required Libraries
from tkinter import *
from tkinter import ttk
from wordle_solver import *


a_file = open("words.txt")
file_contents = a_file.read()

words = file_contents.splitlines()


def contains():
   global words
   letters = entry.get()
   matches = []
   count = 0
   for word in words:
     for letter in letters:
         if letter in word:
             count += 1
     if count == len(letters):
         matches.append(word)
     count = 0

   words = matches
   print(words)
   # return words


def contains_at_index():
   global words
   data = entry.get().split(',')
   letter = data[0]
   index = int(data[1])
   matches = []
   for word in words:
     if word[index] == letter:
         matches.append(word)

   words = matches
   print(words)
   # return matches


def not_contains():
   global words
   letter = entry.get()
   x = []
   for word in words:
     if letter not in word:
         x.append(word)
     else:
         pass
   print(x)
   words = x
   # return x


def not_contains_at_index():
   global words
   data = entry.get().split(',')
   letter = data[0]
   index = int(data[1])
   x = []
   for word in words:
     if word[index] != letter:
         x.append(word)
     else:
         pass

   words = x
   print(words)


def remove_word():
   global words
   word = entry.get()
   words.remove(word)
   print(words)


def reset_words():
   global words
   a_file = open("words.txt")
   file_contents = a_file.read()
   words = file_contents.splitlines()


win= Tk()
win.geometry("750x500")


def wordle_sort(mode: str):
   string= entry.get()
   label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
global entry
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text="Contains", width=40, command=contains).pack(pady=5)
ttk.Button(win, text="Contains at Index", width=40, command=contains_at_index).pack(pady=5)
ttk.Button(win, text="Doesn't Contain", width=40, command=not_contains).pack(pady=5)
ttk.Button(win, text="Doesn't Contains at index", width=40, command=not_contains_at_index).pack(pady=5)
ttk.Button(win, text="Remove Word", width=40, command=remove_word).pack(pady=5)
ttk.Button(win, text="Reset", width=40, command=reset_words).pack(pady=5)

win.mainloop()