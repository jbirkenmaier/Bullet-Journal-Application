import tkinter as tk
import matplotlib.pyplot as plt
import customtkinter as ctk
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

activities=[]

def printInput(root,inputtxt): 
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    label = tk.Label(root, text = inp)
    #label.pack()

def create_activity():
    pass


def on_enter(left_frame,right_frame,event, inputtxt):
    #printInput(root,inputtxt)
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    if inp != "":
        activity = Activity(right_frame,inputtxt, 0,0).plot_graph()
        activities.append(activity)
        ctk.set_default_color_theme("blue")
        activity_button = ctk.CTkButton(master=left_frame, text=inp)
        activity_button.grid(row=len(activities)+10, column=1,sticky="nsew", pady=1)
        #activity_label = tk.Label(left_frame,text=inp, font = ("Verdana 10 bold", 25),fg = "blue",bg = "yellow")
        #activity_label.grid(row=len(activities)+10, column=1,sticky="nsew", pady=1)
    else:
        pass
    
def get_button_width(button, inputtxt):
    add_activity_button_width = button.winfo_width()
    inputtxt.place(x=50+add_activity_button_width+90, y=50)

def add_activity_button_command(left_frame,right_frame,event,inputtxt):
    #printInput(root,inputtxt)
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    if inp != "":
        activity = Activity(right_frame,inputtxt, 0,0).plot_graph()
        activities.append(activity)
        ctk.set_default_color_theme("blue")
        activity_button = ctk.CTkButton(master=left_frame, text=inp)
        activity_button.grid(row=len(activities)+10, column=1,sticky="nsew", pady=1)
        #activity_label = tk.Label(left_frame,text=inp, font = ("Verdana 10 bold", 25),fg = "blue",bg = "yellow")
        #activity_label.grid(row=len(activities)+10, column=1,sticky="nsew", pady=1)
    else:
        pass
    inputtxt.delete(1.0, ctk.END)

class Activity:
    def __init__(self, root, name, row, column):
        self.root = root
        self.name = name
        self.row = row
        self.column = column
        self.plot_graph()
        #self.goal (daily, weekly,monthly)
        
    def plot_graph(self):
        
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
        canvas.get_tk_widget().grid(row=self.row, column=self.column)



