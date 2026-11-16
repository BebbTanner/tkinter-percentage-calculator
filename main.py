'''
    For this I just want to create a simple percentage calculator.
    I will then take this and use it in my rock paper scissors program.

    This now does what I want it to do.
    I now need to figure out how to implement this with the rock, paper, scissors program.
'''
# Libraries

import customtkinter as ctk
from tkinter import *

# UI setup

root = ctk.CTk()
root.title("Percentages")
root.geometry("500x400")
root.config(bg="#a9a9a9")

# Navbar container

navbar = ctk.CTkFrame(root, fg_color="#2c3e50", height = 50)
navbar.pack(side = "top", fill = "x")
navbar.pack_propagate(False)

navContainer = ctk.CTkFrame(navbar, fg_color="#2c3e50")
navContainer.pack(expand = True, fill = "y")

# Functions

def percentage():
    userX = float(xLabel.get())
    userY = float(yLabel.get())
    result = (userX / userY) * 100

    resultLabel.configure(text=f"Result = {result:.2f}%")

# Labels

resultLabel = ctk.CTkLabel(root, text="Result: ", fg_color="#a9a9a9", text_color="black")
resultLabel.pack(padx=10, pady=10)

# Buttons

xLabel = ctk.CTkEntry(
    navContainer,
)
xLabel.pack(side="left", padx=10, pady=10)

yLabel = ctk.CTkEntry(
    navContainer,
)
yLabel.pack(side="left", padx=10, pady=10)

calculate = ctk.CTkButton(    
    navContainer, 
    text="Calculate",
    command= percentage,
    fg_color="#2b8a3e",
    hover_color="#237032")
calculate.pack(side="left", padx=10, pady=10)

# Main loop

root.mainloop()