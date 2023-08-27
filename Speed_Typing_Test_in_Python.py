from time import time
from tkinter import *
from tkinter import messagebox
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    speed = len(userinput) / time_delay
    return round(speed,2)

def result(event=None):
    # test1 as global here for updation when we submit the result it show new sentences
    global test1  
    user_input = testinput.get("1.0", "end-1c")
    speed = speed_time(time_1, time(), user_input)
    mistakes = mistake(test1, user_input)
    
    result_text = f"Speed: {speed:.2f} characters per second\nMistakes: {mistakes}"
    messagebox.showinfo("Result", result_text)
    
    # Reset the window
    testinput.delete("1.0", "end")
    
    # Update test1 with a new test sentence
    test1 = r.choice(test)  
    text_label.config(text=test1)

def close_win():
    root.destroy()

root = Tk()
root.title("Typing Speed Test")

Label(text="Typing Speed Test", font="lucida 25 bold").pack()

test = [
    "Python is a high-level, general-purpose programming language",
    "C++ is a high-level, general-purpose programming language created by Danish computer scientist Bjarne Stroustrup.",
    "Tkinter is a Python binding to the Tk GUI toolkit",
    "Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible"
]

test1 = r.choice(test)

# For showing the text on the screen
f = Frame(root, bg="white")
f.pack(pady=20, anchor="n")
text_label = Label(f, text=test1, font="Ubuntu 20", wraplength=1200)
text_label.pack()

# User Input
Label(text="Write the above Line", font="lucida 25 bold").pack(pady=10)

# taking the user input
testinput = Text(root, font="Ubuntu 20", height=10, width=40)
testinput.pack(fill=BOTH, pady=30)

# Create a submit button
button = Button(root, text="Submit it!!", font="lucida 15 bold", command=result)
button.pack()

# Create a delete button to close the window
button1 = Button(root, text=" Close ", font="lucida 15 bold", command=close_win)
button1.pack(pady=10)

time_1 = time()

root.mainloop()
