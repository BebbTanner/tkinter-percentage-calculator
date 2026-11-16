'''
    For this I just want to create a simple percentage calculator.
    I will then take this and use it in my rock paper scissors program.
'''

import tkinter as tk
from tkinter import *

# UI setup

root = tk.Tk()
root.title("Percentages")
root.geometry("500x400")
root.config(bg="#a9a9a9")

# Functions

def percentage():
    print()

# Styling

# Buttons

calculateButton = tk.Button(root, text="Calculate", command= percentage)
calculateButton.pack(padx=10, pady=10)

# Labels

resultLabel = tk.Label(root, text="Your percentage is: ")
resultLabel.pack(padx=10, pady=10)

# Main loop

root.mainloop()