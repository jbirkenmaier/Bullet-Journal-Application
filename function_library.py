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

def load_state(root1,root2):
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
        for element in main.activities:
            file.write(str(element.name)+",")
            file.write(str(element.row)+",")
            file.write(str(element.column)+",")
            file.write(str(element.time)+",")
            file.write(str(element.unit)+",")
            file.write(str(element.x)+",")
            file.write(str(element.y)+"\n")
 
def printInput(root,inputtxt): 
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    label = tk.Label(root, text = inp)

def read_data(left_frame,right_frame,event, user_data, row, date_data_exists = False, u_data_date = None, time_data_exists=False, u_data_time=None):
    try:
        inp = user_data.get("end-1c linestart", "end-1c lineend")
    except:
        if type(user_data)==str:
            inp=user_data
            print('type gets passed as string, not as Text-object, this can be cause for errors')
        else:
            print('something went wrong')

    try:
        inp_u_data_date =  u_data_date.get("end-1c linestart", "end-1c lineend")
    except:
        if type(u_data_date)==str:
            inp_u_data_date = u_data_date
            print('type gets passed as string, not as Text-object, this can be cause for errors')

        else:
            print('something went wront')

    if (date_data_exists == True) and (inp == ""):
        print("Data Missing! Just given a date")
        return
    elif(date_data_exists == True) and (inp_u_data_date == ""):
        print("Date Missing! Just given data")
        return


    list_position_of_activity = row-11

    if u_data_time != None:
        try:
            inp_u_data_time = u_data_time.get("end-1c linestart", "end-1c lineend")
        except:
            if type(u_data_time) == str:
                inp_u_data_time = u_data_time
                print('type gets passed as string, not as Text-object, this can be cause for errors')
            else:
                print('something went wrong')
    clear_line(user_data)
    clear_line(u_data_date)
    clear_line(u_data_time)

    current_time= str(datetime.datetime.now().time().strftime("%H:%M"))
    u_data_time.insert("end",current_time)
    u_data_time.mark_set(tk.INSERT, "1.0")

    current_date = str(datetime.datetime.now().date().strftime("%d.%m.%Y"))
    u_data_date.insert("end",current_date)
    
    if date_data_exists == False and inp!= "": #if no date_data_exists and input is given, the current date is assumed
        main.activities[list_position_of_activity].y.append(float(inp))
        main.activities[list_position_of_activity].time=datetime.datetime.now()
        main.activities[list_position_of_activity].append_time()
        main.activities[list_position_of_activity].plot_graph()    
        save_state()
    elif (date_data_exists == True) and (inp != "") and (time_data_exists==True): #if date_data_exists and time_data_exists and input is given, it will be handled accordingly
        u_day, u_month, u_year = map(int, inp_u_data_date.split('.'))
        u_hour , u_minute = map(int, inp_u_data_time.split(':'))

        main.activities[list_position_of_activity].y.append(float(inp))
        main.activities[list_position_of_activity].time=datetime.datetime.now()
        main.activities[list_position_of_activity].append_time()
        main.activities[list_position_of_activity].x[-1] = main.activities[list_position_of_activity].x[-1].replace(day = u_day, month=u_month, year=u_year, hour=u_hour, minute=u_minute)##################
        reorder(main.activities[list_position_of_activity])
        main.activities[list_position_of_activity].plot_graph()    
        save_state()


def reorder(activity):
    original_state_x = activity.x
    original_state_y = activity.y
    sorted_indices = sorted(range(len(original_state_x)), key=lambda x: original_state_x[x])
    activity.x = [original_state_x[i] for i in sorted_indices]
    activity.y = [original_state_y[i] for i in sorted_indices]

def clear_line(text_widget):
    try:
        text_widget.delete("insert linestart", "insert lineend")
    except:
        pass
    
def activity_button_event(left_frame,right_frame, event, inputtxt, row):
    user_data = tk.Text(left_frame, height = 1, width = 5, bg="lightgray", padx=10, pady=5)
    user_data.grid(row=row, column =2)

    current_date = str(datetime.datetime.now().date().strftime("%d.%m.%Y"))
    user_data_date = tk.Text(left_frame, height = 1, width = 10, bg="lightgray", padx=3, pady=5)
    user_data_date.grid(row=row, column =3)
    user_data_date.insert("end",current_date)

    current_time= str(datetime.datetime.now().time().strftime("%H:%M"))
    user_data_time = tk.Text(left_frame, height = 1, width = 10, bg="lightgray", padx=3, pady=5)
    user_data_time.grid(row=row, column =4)
    user_data_time.insert("end",current_time)

    inp_truth = user_data.bind("<Return>",lambda event: process_user_input(left_frame,right_frame,event,[user_data, user_data_date, user_data_time],row))
    inp_truth = user_data_date.bind("<Return>",lambda event: process_user_input(left_frame,right_frame,event, [user_data, user_data_date, user_data_time],row))
    inp_truth = user_data_time.bind("<Return>",lambda event: process_user_input(left_frame,right_frame,event, [user_data, user_data_date, user_data_time],row))
    

def process_user_input(left_frame, right_frame, event, inp_list, row):
    (inp_truth,inp_data) = check_for_input(left_frame, right_frame, event, inp_list)
    user_data_exists = inp_truth[0]
    date_data_exists = inp_truth[1]
    time_data_exists = inp_truth[2]

    user_data = inp_list[0]
    user_data_date = inp_list[1]
    user_data_time = inp_list[2]

    if user_data_exists == 1 and date_data_exists==1 and time_data_exists == 1:
        read_data(left_frame,right_frame,event, user_data, row, date_data_exists=date_data_exists, u_data_date=user_data_date, u_data_time=user_data_time, time_data_exists = time_data_exists)
   

def check_for_input(left_frame,right_frame,event, inp_list): #takes inputs as list

    inp_truth=[]
    inp_data =[]
    
    for element in inp_list:
        inp = element.get("end-1c linestart", "end-1c lineend")
        if inp != "":
            inp_value = True
            inp_data.append(inp)
        else:
            inp_value = False
            inp_data.append('')
        inp_truth.append(inp_value)
    return inp_truth, inp_data
    
def get_button_width(button, inputtxt):
    add_activity_button_width = button.winfo_width()
    inputtxt.place(x=50+add_activity_button_width+90, y=50)

def add_activity_button_command(left_frame,right_frame,event,inputtxt):
    printInput(left_frame, inputtxt)
    on_enter(left_frame,right_frame,event,inputtxt)
    clear_line(inputtxt)

class Activity:
    def __init__(self, root, name, row, column):
        self.root = root
        self.name = name
        self.row = row
        self.column = column
        self.time = None
        self.unit = " "
        self.x = []
        self.y= []
        self.indx = len(main.activities)
        #self.goal(daily, weekly,monthly) #Future attribute 
        
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


