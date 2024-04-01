import function_library as fl
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

font_size = 25  


def main():
    root = ctk.CTk()
    #app = BulletJournalApp(root)
    root.title("Journal-Application")
    root.geometry("1000x500")

    font = tk.font.Font(size=font_size)
    
    
    # Create a frame for the left part
    left_frame = tk.Frame(root,bg="black")
    left_frame.grid(row=0, column=0, sticky="nsew")

    # Create a frame for the right part
    right_frame = tk.Frame(root, bg="black")
    right_frame.grid(row=0, column=1, sticky="nsew")

    # Ensure resizing behavior
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    
    inputtxt = tk.Text(left_frame, height = 1, width = 20, font=font,bg="lightgray", padx=10, pady=5)
    #inputtxt.pack()
    #inputtxt.place(x=100, y=50)
    inputtxt.grid(row=0, column=0)
    inputtxt.bind("<Return>",lambda event: fl.on_enter(root,event, inputtxt))

    

    add_activity_button = ctk.CTkButton(master=left_frame, text="Add activity")
    #add_activity_button.pack()
    #add_activity_button.place(x=50, y=50)
    add_activity_button.grid(row=0, column=1)
    add_activity_button.bind("<Button-1>",lambda event: fl.add_activity_button_command(root, event, inputtxt))
    #add_activity_button.after_idle(lambda: fl.get_button_width(add_activity_button, inputtxt))  # Get button width after it's fully drawn


    activity = fl.Activity(right_frame,"name","typ", 0,0).plot_graph()
    activity = fl.Activity(right_frame,"name","typ", 0,1).plot_graph()
    activity = fl.Activity(right_frame,"name","typ", 1,0).plot_graph()
    activity = fl.Activity(right_frame,"name","typ", 1,1).plot_graph()
    #activity = fl.Activity(right_frame,"name","typ", 2,0).plot_graph()
    #activity = fl.Activity(right_frame,"name","typ", 2,1).plot_graph()
    #activity = fl.Activity(right_frame,"name","typ", 0,2).plot_graph()
    #activity = fl.Activity(right_frame,"name","typ", 1,2).plot_graph()

    # Configure resizing behavior
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
        
    root.mainloop()

if __name__ == "__main__":
    main()
