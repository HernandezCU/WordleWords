#Import the required Libraries
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from wordle_solver import *


a_file = open("words.txt")
file_contents = a_file.read()

words = file_contents.splitlines()


def suggestions():
    count = {'a': 979, 'b': 281, 'c': 477, 'd': 393, 'e': 1233, 'f': 230, 'g': 311, 'h': 389, 'i': 671, 'j': 27,
             'k': 210, 'l': 719, 'm': 316, 'n': 575, 'o': 754, 'p': 367, 'q': 29, 'r': 899, 's': 669, 't': 729,
             'u': 467, 'v': 153,'w': 195, 'x': 37, 'y': 425, 'z': 40}

    max = {'e': 1233, 'a': 979, 'r': 899, 'o': 754, 't': 729}

    min = {'j': 27, 'q': 29, 'x': 37, 'z': 40, 'v': 153}


    label.configure(text="Most common: " + str(max))
    label2.configure(text= "Least Common: "+ str(min))
    st.insert('end', ';')


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
win.title("Wordle Solver")


label=Label(win, text="", font=("Times New Roman", 12))
label.pack()
label2=Label(win, text="", font=("Times New Roman", 12))
label2.pack()


global entry
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text="Contains", width=40, command=contains).pack(pady=5)
ttk.Button(win, text="Contains at Index", width=40, command=contains_at_index).pack(pady=5)
ttk.Button(win, text="Doesn't Contain", width=40, command=not_contains).pack(pady=5)
ttk.Button(win, text="Doesn't Contains at index", width=40, command=not_contains_at_index).pack(pady=5)
ttk.Button(win, text="Remove Word", width=40, command=remove_word).pack(pady=5)
ttk.Button(win, text="Reset", width=40, command=reset_words).pack(pady=5)
ttk.Button(win, text="Suggest Word", width=40, command=suggestions).pack(pady=5)

global st
st = ScrolledText(win, width=50,  height=10)
st.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
st.configure(state="disabled")

win.mainloop()