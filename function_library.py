import tkinter as tk
import matplotlib.pyplot as plt
import customtkinter as ctk
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%d.%m.%Y %H:%M:%S")
print("Formatted Time:", formatted_time)

activities=[]

row = 0
column = 0
first_run=True

def save_state():
    with open('data.txt', 'w') as f:
        print("Datenlänge:",len(activities))
        for element in activities:
            f.write(str(element.name))
            f.write(str(element.row))
            f.write(str(element.column))
            f.write(str(element.time))
            f.write(str(element.unit))
            f.write(str(element.x))
            f.write(str(element.y))

        # Pickle the 'data' dictionary using the highest protocol available.
        
def load_state():
    with open('data.txt', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
        activities = pickle.load(f)

def printInput(root,inputtxt): 
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    label = tk.Label(root, text = inp)
    #label.pack()

def read_data(left_frame,right_frame,event, user_data, row):
    list_position_of_activity = row-10
    inp = user_data.get("end-1c linestart", "end-1c lineend")
    activities[list_position_of_activity-1].y.append(float(inp))
    activities[list_position_of_activity-1].plot_graph()
    save_state()
    #print(list_position_of_activity)
    #print(activities[list_position_of_activity-1].name)
    #print(activities[list_position_of_activity-1].time.year)

def activity_button_event(left_frame,right_frame, event, inputtxt, row):
    user_data = tk.Text(left_frame, height = 1, width = 5, bg="lightgray", padx=10, pady=5)
    user_data.grid(row=row, column =2)
    user_data.bind("<Return>",lambda event: read_data(left_frame,right_frame,event, user_data, row))
    

def on_enter(left_frame,right_frame,event, inputtxt):
    #printInput(root,inputtxt)
    global row, column, first_run
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    if inp != "":
        if column==2:
            print(row,column)
            activity = Activity(right_frame,inp, row,column)
            activity.time = datetime.datetime.now()
            activities.append(activity)
            #activity.plot_graph()
            column=0
            row+=1
        else:
            print(row,column)
            activity = Activity(right_frame,inp, row,column)
            activity.time = datetime.datetime.now()
            activities.append(activity)
            #activity.plot_graph()
            column+=1
        ctk.set_default_color_theme("blue")
        activity_button = ctk.CTkButton(master=left_frame, text=inp)
        rows=len(activities)+10
        activity_button.grid(row=rows, column=1,sticky="nsew", pady=1)
        activity_button.bind("<Button-1>",lambda event: activity_button_event(left_frame,right_frame, event, inputtxt, rows))
        save_state()
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
        activity = Activity(right_frame,inp, 0,0)
        activity.time = datetime.datetime.now()
        activities.append(activity)
        activity.plot_graph()
        ctk.set_default_color_theme("blue")
        activity_button = ctk.CTkButton(master=left_frame, text=inp)
        row=len(activities)+10
        activity_button.grid(row=row, column=1,sticky="nsew", pady=1)
        activity_button.bind("<Button-1>",lambda event: activity_button_event(left_frame,right_frame, event, inputtxt, row))
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
        #self.plot_graph()
        self.time = None
        self.unit = " "
        self.x = []
        self.y=[]
        #self.goal (daily, weekly,monthly)
        
    def plot_graph(self):
        
        #x=[i for i in range(4)]
        #y=[random.randint(-10,10) for i in range(4)]

        self.append_time()
        
        x=self.x
        y=self.y
        
        fig = Figure(figsize=(5, 4), dpi=100)
        plot = fig.add_subplot(1, 1, 1)
        plot.plot(x,y, marker='o')
        plot.set_title(self.name)
        plot.set_xlabel('Datum')
        plot.set_ylabel(self.unit)

        plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%Y'))

        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=self.row, column=self.column)

    def append_time(self):
        self.x.append(self.time)


