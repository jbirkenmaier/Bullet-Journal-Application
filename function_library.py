import tkinter as tk
import matplotlib.pyplot as plt
import customtkinter as ctk
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def printInput(root,inputtxt): 
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    label = tk.Label(root, text = inp)
    #label.pack()

def on_enter(root,event, inputtxt):
    printInput(root,inputtxt)

def get_button_width(button, inputtxt):
    add_activity_button_width = button.winfo_width()
    inputtxt.place(x=50+add_activity_button_width+90, y=50)

def add_activity_button_command(root,event,inputtxt):
    printInput(root,inputtxt)
    inputtxt.delete(1.0, ctk.END)

class Activity:
    def __init__(self, root, name, typ, row, column):
        self.root = root
        self.name = name
        self.typ = typ
        self.row = row
        self.column = column
        self.plot_graph()
        
    def plot_graph(self):
        #plot_frame = tk.Frame(self.root)
        #plot_frame.grid(row=self.row, column=self.column)

        x=[i for i in range(4)]
        y=[random.randint(-10,10) for i in range(4)]

        fig = Figure(figsize=(5, 4), dpi=100)
        plot = fig.add_subplot(1, 1, 1)
        plot.plot(x,y, marker='o')
        plot.set_title('Example Plot')
        plot.set_xlabel('X-axis')
        plot.set_ylabel('Y-axis')
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=self.row, column=self.column)#grid(row=self.row, column=self.column)

        # Place the canvas on the Tkinter window
        #canvas.get_tk_widget().place(x=100, y=200)

        #canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        #canvas.draw()
        #canvas.get_tk_widget().pack(side="top", fill="both", expand=False)


