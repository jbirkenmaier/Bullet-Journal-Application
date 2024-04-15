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
import main

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%d.%m.%Y %H:%M:%S")


def on_enter(left_frame,right_frame,event, inputtxt, get_txt=True, activity=None):

    if get_txt==True:
        inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    else:
        inp = inputtxt

    if inp != "" and get_txt==True:
        if main.column==2:
            activity = Activity(right_frame,inp, main.row, main.column) 
            activity.time = datetime.datetime.now()
            main.activities.append(activity)
            activity.plot_graph()
            main.column=0
            main.row+=1
        else:
            activity = Activity(right_frame,inp, main.row,main.column) 
            activity.time = datetime.datetime.now()
            main.activities.append(activity)
            activity.plot_graph()
            main.column+=1
        ctk.set_default_color_theme("blue")
        activity_button = ctk.CTkButton(master=left_frame, text=inp)
        rows=activity.indx+11
        activity_button.grid(row=rows, column=1,sticky="nsew", pady=1)
        activity_button.bind("<Button-1>",lambda event: activity_button_event(left_frame,right_frame, event, inputtxt, rows))
        activity.plot_graph()
        save_state()
        
    elif get_txt==False:
        ctk.set_default_color_theme("blue")
        activity_button = ctk.CTkButton(master=left_frame, text=inp)
        rows=activity.indx+11
        activity_button.grid(row=rows, column=1,sticky="nsew", pady=1)
        activity_button.bind("<Button-1>",lambda event: activity_button_event(left_frame,right_frame, event, inputtxt, rows))
        activity.plot_graph()
        save_state()
        ctk.set_default_color_theme("green")
    else:
        pass

def load_state(root1,root2):#call root as right_frame
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
            rw = int(line[1].strip())
            cm = int(line[2].strip())

            x_ev = []
            y_ev = []
            
            for i in range(number_of_entrys):
                date_str = line[date_index_positions[i]:date_index_positions[i]+7]
                date_str = ",".join(date_str).strip().strip("[datetime.datetime(").strip(")]")
                date_obj=datetime.datetime.strptime(date_str, '%Y, %m, %d, %H, %M, %S, %f')
                x_ev.append(date_obj)
                y_str = line[-(i+1)].strip().strip(']').strip('[')
                y_ev.append(ast.literal_eval(y_str))

            y_ev.reverse()
            
            activity = Activity(root2,act,rw,cm)
            #activity.time = ast.literal_eval((line[3]))
            activity.unit = line[4]
            activity.x = x_ev
            activity.y = y_ev
            main.activities.append(activity)
    for (i,element) in enumerate(main.activities):
        element.indx = i
        on_enter(root1, root2,"",element.name, get_txt=False, activity=element)
    set_row_col()

def set_row_col():
    if main.activities!=[]:
        if main.activities[-1].column==2:
            main.row=main.activities[-1].row+1
            main.column=0
        else:
            main.row=main.activities[-1].row
            main.column+=1
        
def save_state():
    with open('data.csv', 'w') as file:
        #print("Datenlänge:",len(main.activities))
        for element in main.activities:
            file.write(str(element.name)+",")
            file.write(str(element.row)+",")
            file.write(str(element.column)+",")
            file.write(str(element.time)+",")
            file.write(str(element.unit)+",")
            file.write(str(element.x)+",")
            file.write(str(element.y)+"\n")

        # Pickle the 'data' dictionary using the highest protocol available.
        

    
def printInput(root,inputtxt): 
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    label = tk.Label(root, text = inp)
    #label.pack()

def read_data(left_frame,right_frame,event, user_data, row):
    list_position_of_activity = row-11
    #print("MARKER, ",list_position_of_activity, len(main.activities))
    inp = user_data.get("end-1c linestart", "end-1c lineend")

    main.activities[list_position_of_activity].y.append(float(inp))
    main.activities[list_position_of_activity].time=datetime.datetime.now()
    main.activities[list_position_of_activity].append_time()
    main.activities[list_position_of_activity].plot_graph()    
    save_state()

def activity_button_event(left_frame,right_frame, event, inputtxt, row):
    user_data = tk.Text(left_frame, height = 1, width = 5, bg="lightgray", padx=10, pady=5)
    user_data.grid(row=row, column =2)
    user_data.bind("<Return>",lambda event: read_data(left_frame,right_frame,event, user_data, row))


'''    

def on_enter(left_frame,right_frame,event, inputtxt, get_txt=True, activity=None):
    #printInput(root,inputtxt)
    global row, column, first_run
    if get_txt==True:
        inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    else:
        inp = inputtxt

#BUG: I hardcoded the rows and columns here. But if data is loaded, then this wont work anymore.
#Solution: Start from the smallest rows and columns

    if inp != "" and get_txt==True:
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
        
    elif get_txt==False:
        print('CALLED')
        ctk.set_default_color_theme("blue")
        activity_button = ctk.CTkButton(master=left_frame, text=inp)
        rows=activity.indx+10
        activity_button.grid(row=rows, column=1,sticky="nsew", pady=1)
        activity_button.bind("<Button-1>",lambda event: activity_button_event(left_frame,right_frame, event, inputtxt, rows))
        activity.plot_graph()
        save_state()
        ctk.set_default_color_theme("green")


        #activity_label = tk.Label(left_frame,text=inp, font = ("Verdana 10 bold", 25),fg = "blue",bg = "yellow")
        #activity_label.grid(row=len(activities)+10, column=1,sticky="nsew", pady=1)
    else:
        pass



def load_state(root1,root2):#call root as right_frame
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
            
            activity = Activity(root2,act,rw,cm)
            #activity.time = ast.literal_eval((line[3]))
            activity.unit = line[4]
            activity.x = x_ev
            activity.y = y_ev
            activities.append(activity)
    for (i,element) in enumerate(activities):
        element.indx = i
        on_enter(root1, root2,"",element.name, get_txt=False, activity=element)
    set_row_col()
    return activities
'''
    
def get_button_width(button, inputtxt):
    add_activity_button_width = button.winfo_width()
    inputtxt.place(x=50+add_activity_button_width+90, y=50)

def add_activity_button_command(left_frame,right_frame,event,inputtxt):
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    if inp != "":
        if main.column==2:
            activity = Activity(right_frame,inp, main.row, main.column)
            activity.time = datetime.datetime.now()
            main.activities.append(activity)
            activity.plot_graph()
            main.column=0
            main.row+=1
        else:
            activity = Activity(right_frame,inp, main.row,main.column) 
            activity.time = datetime.datetime.now()
            main.activities.append(activity)
            activity.plot_graph()
            main.column+=1
        ctk.set_default_color_theme("blue")
        activity_button = ctk.CTkButton(master=left_frame, text=inp)
        rows=activity.indx+11
        activity_button.grid(row=rows, column=1,sticky="nsew", pady=1)
        activity_button.bind("<Button-1>",lambda event: activity_button_event(left_frame,right_frame, event, inputtxt, rows))
        activity.plot_graph()
        save_state()
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
        self.indx = len(main.activities)
        #self.goal (daily, weekly,monthly)
        
    def plot_graph(self):
        
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


