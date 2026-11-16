'''
    For this I just want to create a simple percentage calculator.
    I will then take this and use it in my rock paper scissors program.

    This now does what I want it to do.
    I now need to figure out how to implement this with the rock, paper, scissors program.
'''
# Libraries

import tkinter as tk
import customtkinter as ctk
from tkinter import *

# UI setup

root = tk.Tk()
root.title("Percentages")
root.geometry("500x400")
root.config(bg="#a9a9a9")

# Navbar container

navbar = tk.Frame(root, bg = "#2c3e50", height = 50)
navbar.pack(side = "top", fill = "x")
navbar.pack_propagate(False)
navContainer = tk.Frame(navbar, bg = "#2c3e50")
navContainer.pack(expand = True, fill = "y")

# Functions

def percentage():
    userX = float(xLabel.get())
    userY = float(yLabel.get())
    result = (userX / userY) * 100

    resultLabel.config(text=f"Result = {result:.2f}%")

# Labels

xLabel = tk.Entry(root, width=10)
xLabel.pack(padx=10, pady=10)

yLabel = tk.Entry(root, width=10)
yLabel.pack(padx=10, pady=10)

resultLabel = tk.Label(root, text="Your percentage is: ")
resultLabel.pack(padx=10, pady=10)

# Buttons

calculateButton = ctk.CTkEntry(
    navbar,
    corner_radius=32,
)
calculateButton.pack(side="left", padx=10, pady=10)

calculateButton = ctk.CTkButton(
    navbar, text="Calculate",
    command= percentage,
    fg_color="#2b8a3e",
    corner_radius=32,
    hover_color="#237032"
)
calculateButton.pack(side="left", padx=10, pady=10)


# Main loop

root.mainloop()