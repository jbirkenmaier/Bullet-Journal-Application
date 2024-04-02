import function_library as fl
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

font_size = 25  

activities = []

def main():
    root = ctk.CTk()
    #app = BulletJournalApp(root)
    root.title("Journal-Application")
    root.geometry("1000x500")

    font = tk.font.Font(size=font_size)
    
    left_frame = tk.Frame(root,bg="black")
    left_frame.grid(row=0, column=0, sticky="nsew")

    right_frame = tk.Frame(root, bg="black")
    right_frame.grid(row=0, column=1, sticky="nsew")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    
    inputtxt = tk.Text(left_frame, height = 1, width = 20, font=font,bg="lightgray", padx=10, pady=5)
    inputtxt.grid(row=1, column=2)
    inputtxt.bind("<Return>",lambda event: fl.on_enter(left_frame,right_frame,event, inputtxt))

    add_activity_button = ctk.CTkButton(master=left_frame, text="Add Activity")
    add_activity_button.grid(row=2, column=2)
    add_activity_button.bind("<Button-1>",lambda event: fl.add_activity_button_command(left_frame,right_frame, event, inputtxt))

    for row in range(3,10):
        tk.Frame(left_frame,width=183, height=20, bg="black").grid(row=row, column=1, sticky="nsew")
    

    #add_activity_button.after_idle(lambda: fl.get_button_width(add_activity_button, inputtxt))  # Get button width after it's fully drawn

    '''
    activity = fl.Activity(right_frame,"name", 0,0).plot_graph()
    activity = fl.Activity(right_frame,"name", 0,1).plot_graph()
    activity = fl.Activity(right_frame,"name", 1,0).plot_graph()
    activity = fl.Activity(right_frame,"name", 1,1).plot_graph()
    '''

        
    root.mainloop()

if __name__ == "__main__":
    main()
