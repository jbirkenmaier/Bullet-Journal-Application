import function_library as fl
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

font_size = 25  


def main():
    root = ctk.CTk()
    font = tk.font.Font(size=font_size)
    
    #app = BulletJournalApp(root)
    root.title("Input Window")
    root.geometry("1000x500")

    inputtxt = tk.Text(root, height = 1, width = 50, font=font)
    inputtxt.pack()
    inputtxt.place(x=100, y=50)
    inputtxt.bind("<Return>",lambda event: fl.on_enter(root,event, inputtxt))

    add_activity_button = ctk.CTkButton(master=root, text="Add activity")
    add_activity_button.pack()
    add_activity_button.place(x=50, y=50)
    add_activity_button.bind("<Button-1>",lambda event: fl.add_activity_button_command(root, event, inputtxt))
    #add_activity_button.after_idle(lambda: fl.get_button_width(add_activity_button, inputtxt))  # Get button width after it's fully drawn
    
    root.mainloop()

if __name__ == "__main__":
    main()
