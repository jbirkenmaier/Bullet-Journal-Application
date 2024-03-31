import function_library as fl
import tkinter as tk
import matplotlib.pyplot as plt




def printInput(root,inputtxt): 
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    label = tk.Label(root, text = inp)
    label.pack()

def on_enter(root,event, inputtxt):
    printInput(root,inputtxt)

def get_button_width(button, inputtxt):
    add_activity_button_width = button.winfo_width()
    inputtxt.place(x=50+add_activity_button_width+10, y=50)
    
def main():
    root = tk.Tk()
    #app = BulletJournalApp(root)
    root.title("Input Window")
    root.geometry("1000x500")

    inputtxt = tk.Text(root, height = 2, width = 50)
    inputtxt.pack()
    inputtxt.place(x=50, y=50)
    inputtxt.bind("<Return>",lambda event: on_enter(root,event, inputtxt))


    add_activity_button = tk.Button(root, text="Add activity")
    add_activity_button.place(x=50, y=50)
    add_activity_button.after_idle(lambda: get_button_width(add_activity_button, inputtxt))  # Get button width after it's fully drawn
    
    root.mainloop()

if __name__ == "__main__":
    main()
