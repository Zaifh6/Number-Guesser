# importing all the necessary libraries
from tkinter import *
from tkinter import ttk
import random

# creating the random number
RAND_NUM = random.randint(0, 100)
HINT_UP = RAND_NUM + 5
HINT_DOWN = RAND_NUM - 5

# comment this line if you wanna play the game and uncomment this if you wanna test the program
print(RAND_NUM)

# creating tkinter object
win = Tk()

# setting windows title
win.title("Number Guesser Game")

# setting windows width and height
win.geometry("750x250")

# method to check if our answer was correct
def get_value():
   e_text=entry.get()
   if int(e_text) == RAND_NUM:
      Label(win, text=f"{e_text} was correct answer", font= ('Century 15 bold')).pack(pady=20)
   else:
      Label(win, text=f"{e_text} was not the correct answer", font=('Century 15 bold')).pack(pady=20)

# method to display hint
def hint():
   ttk.Label(win, text=f"HINT: the number is less than {HINT_UP} & greater than {HINT_DOWN}").pack()

# input entry
entry= ttk.Entry(win,font=('Century 12'),width=40)
entry.pack(pady= 30)

# enter button
button= ttk.Button(win, text="Enter", command= get_value)
button.pack()

# hint button
hint_button= ttk.Button(win, text="hint", command= hint)
hint_button.pack()

win.mainloop()
