import tkinter as tk
import matplotlib.pyplot as plt
import customtkinter as ctk
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import datetime
import ast
import csv

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%d.%m.%Y %H:%M:%S")
print("Formatted Time:", formatted_time)

activities=[]

row = 0
column = 0
first_run=True

def save_state():
    with open('data.csv', 'w') as file:
        print("Datenlänge:",len(activities))
        for element in activities:
            file.write(str(element.name)+",")
            file.write(str(element.row)+",")
            file.write(str(element.column)+",")
            file.write(str(element.time)+",")
            file.write(str(element.unit)+",")
            file.write(str(element.x)+",")
            file.write(str(element.y)+"\n")

        # Pickle the 'data' dictionary using the highest protocol available.
        
def load_state(root):#call root as right_frame
    with open('data.csv') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            number_of_entrys=str(line).count("datetime.datetime")
            date_index_positions = []

            
            for (i,element) in enumerate(line):
                dates_pos = element.find("datetime.datetime")
                if dates_pos !=-1:
                    date_index_positions.append(i)

            act = line[0].strip()
            print(act)
            print('NUM ENTRYS: ', number_of_entrys)

            rw = int(line[1].strip())
            print(rw)
            cm = int(line[2].strip())
            print(cm)

            x_ev = []
            y_ev = []
            
            for i in range(number_of_entrys):
                print("i=",i)
                date_str = line[date_index_positions[i]:date_index_positions[i]+7]
                date_str = ",".join(date_str).strip().strip("[datetime.datetime(").strip(")]")
                print(date_str)
                print("WORKED")
                date_obj=datetime.datetime.strptime(date_str, '%Y, %m, %d, %H, %M, %S, %f')
                x_ev.append(date_obj)
                y_str = line[7*number_of_entrys+i].strip()
                y_ev.append(ast.literal_eval(y_str))
                
                
                #if y_str != "":
                #    print("Y-String: ", y_str)
                #    y_ev = ast.literal_eval(y_str)
                #else:
                #    y_ev =[]
            



            '''
            if x_str!="":
                x_ev = ast.literal_eval(x_str)
            else:
                x_ev=[]
            ''' 
            #line=line.strip().split('STOP')
            #print(line[0])
            #for element in line:
                #print(element)
            
            activity = Activity(root,act,rw,cm)
            #activity.time = ast.literal_eval((line[3]))
            activity.unit = line[4]
            activity.x = x_ev
            activity.y = y_ev
            activities.append(activity)
    for element in activities:
        element.plot_graph()
    
def printInput(root,inputtxt): 
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    label = tk.Label(root, text = inp)
    #label.pack()

def read_data(left_frame,right_frame,event, user_data, row):
    list_position_of_activity = row-10
    inp = user_data.get("end-1c linestart", "end-1c lineend")
    activities[list_position_of_activity-1].y.append(float(inp))
    activities[list_position_of_activity-1].time=datetime.datetime.now()
    activities[list_position_of_activity-1].append_time()
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
            print(activity.time)
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
        self.y= []
        #self.goal (daily, weekly,monthly)
        
    def plot_graph(self):
        
        #x=[i for i in range(4)]
        #y=[random.randint(-10,10) for i in range(4)]

        #self.append_time()
        
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


