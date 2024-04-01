import tkinter as tk
import matplotlib.pyplot as plt
import customtkinter as ctk

def printInput(root,inputtxt): 
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    label = tk.Label(root, text = inp)
    label.pack()

def on_enter(root,event, inputtxt):
    printInput(root,inputtxt)

def get_button_width(button, inputtxt):
    add_activity_button_width = button.winfo_width()
    inputtxt.place(x=50+add_activity_button_width+90, y=50)

def add_activity_button_command(root,event,inputtxt):
    printInput(root,inputtxt)
    inputtxt.delete(1.0, ctk.END)



