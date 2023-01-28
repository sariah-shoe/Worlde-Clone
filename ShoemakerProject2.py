"""
    A version of wordle created using tkinter
    Filename: ShoemakerProject2
    Author: Sariah Shoemaker
    Date: 1-14-2023
    Course: Intro to Programming 2
    Assignment: Project 2
    Collaborators: None
    Internet Source: I learned to use tkinter last quarter using this tutorial- https://realpython.com/python-gui-tkinter/
"""

import tkinter as tk
import random

"""
        Creates a list of 5 letter words
        parameters: file_path (this variable has the path to the word list)
        return: list (list of 5 letter words)
"""
def word_list(file_path):
    list = []
    # Opens the word list file, splits it into a list, and pulls 5 letter words from that list
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.split("\n")
        for i in content:
            if len(i) == 5:
                list.append(i)
    return(list)

"""
        Checks the users guess
        parameters: win_conditions (a list that keeps track of guesses and if the game has been won), lbl_user(the label that shows users messages), list(the list of 5 lette words), word(the word the user is guessing)
        return: win_conditions
"""
def user_check(win_conditions, lbl_user, list, word):
    # Fetches the user input from the text box
    user_input = user_entry.get()

    # Checks to see if a guess is invalid
    if len(user_input) != 5:
        lbl_user.config(text="Invalid guess")
        return win_conditions

    if user_input not in list:
        lbl_user.config(text="Invalid guess")
        return win_conditions
    
    # If the guess was not invalid, add one to guess counter and reset lbl_user
    win_conditions[0] = win_conditions[0] + 1
    lbl_user.config(text=" ")

    # Goes through each letter in the users guess and compares it to the correct answer
    for i in range(5):
        if user_input[i] == word[i]:
            letter_lbl = tk.Label(master=game_frame,text=user_input[i],bg="green",fg="white",width=5,height=3)
            letter_lbl.grid(row=win_conditions[0], column=i,padx=5,pady=5)
        elif user_input[i] in word:
            letter_lbl = tk.Label(master=game_frame,text=user_input[i],bg="gold",fg="white",width=5,height=3)
            letter_lbl.grid(row=win_conditions[0], column=i,padx=5,pady=5)
        else:
            letter_lbl = tk.Label(master=game_frame,text=user_input[i],bg="gray",fg="white",width=5,height=3)
            letter_lbl.grid(row=win_conditions[0], column=i,padx=5,pady=5)
    
    # Checks end game conditions which are either the user guessing correctly or the user running out of guesses
    if user_input == word:
        entry_button["state"] = "disabled"
        win_conditions[1] = 1
        lbl_user.config(text="That is the correct word! You got it in " + str(win_conditions[0]) + " guesses!")
        return win_conditions

    if win_conditions[0] == 6:
        entry_button["state"] = "disabled"
        lbl_user.config(text="You have run out of guesses")
        return win_conditions

#Creates the word the user is guessing
list = word_list(r"C:\Users\cats1\Documents\Python Projects\usaWords.txt")
word = random.choice(list)
print(word)
win_conditions=[0,0]

#Creates window
window = tk.Tk()
window.rowconfigure([0,2], weight=1)
window.columnconfigure(0, weight=1)

#Creates label frame
label_frame = tk.Frame()
label_frame.grid(row=0, column=0)

game_label = tk.Label(master=label_frame, text="Knock Off Wordle", bg="gray", fg="white")
game_label.grid(row=0, column=0,sticky="ewns")

#Creates game frame
game_frame = tk.Frame()
game_frame.grid(row=1, column=0)

#Creates user interaction frame
user_frame = tk.Frame()
user_frame.grid(row=2, column=0)

user_entry = tk.Entry(master=user_frame)
user_entry.grid(row=0, column=0)

lbl_user = tk.Label(master=user_frame, text=" ")
lbl_user.grid(row=1,column=0)

entry_button = tk.Button(master=user_frame, text="Enter", command = lambda:user_check(win_conditions, lbl_user, list, word))
entry_button.grid(row=0,column=1)

window.mainloop()

