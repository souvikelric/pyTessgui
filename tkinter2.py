import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog




root = ctk.CTk()
root.title("Frame App")
root.geometry("600x350")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)


curr_frame = ""
file_str = tk.StringVar(value="File Path shown here")
status_str = tk.StringVar(value="Not Started")
progress = tk.DoubleVar(value=0.5)


def choose_file():
    status_str.set("Template not set")
    filepath = filedialog.askopenfilename()
    if filepath:
        global selected_file
        selected_file = filepath
        file_str.set(selected_file)
        status_str.set("Template set")

def login_screen():
    global curr_frame
    curr_frame = ctk.CTkFrame(root,fg_color="#333",corner_radius=0)
    curr_frame.grid(row=0,column=0,sticky="nsew")

    img = tk.PhotoImage(file="login2.png")
    tk.Label(curr_frame,image=img,bg="white").place(x=50,y=50);
    #create widgets
    # label1 = ctk.CTkLabel(curr_frame, text="Login",text_color="white",font=("Calibri",24),bg_color="transparent")
    # label1.pack(pady=20)
    # button1 = ctk.CTkButton(curr_frame,text="Submit",text_color="white",font=("Calibri",24),command=lambda: switch_screen(main_screen),corner_radius=10,fg_color="#ff10ff")
    # button1.pack(pady=20,ipadx=0,ipady=0)

def main_screen():
    global curr_frame
    curr_frame = ctk.CTkFrame(root,fg_color="#d6ccc2",corner_radius=0)
    curr_frame.grid(row=0,column=0,sticky="nsew")

    #create widgets
    label1 = ctk.CTkLabel(curr_frame, text="Welcome to the main Screen",text_color="#333",font=("Calibri",24,"bold"))
    label1.pack(pady=20)

    input_Frame = ctk.CTkFrame(curr_frame,fg_color="#333",height=90)
    input_Frame.pack(pady=20,padx=20,expand=True,fill="x")
    input_Frame.columnconfigure(0, weight=1)
    input_Frame.columnconfigure(1, weight=1)
    input_Frame.rowconfigure(0, weight=1)

    file_label = ctk.CTkLabel(input_Frame, text="File Path",text_color="#fff",font=("Calibri",15),textvariable=file_str,wraplength=270)
    file_label.grid(row=0,column=0,pady=20)

    file_button = ctk.CTkButton(input_Frame,text="Get File",text_color="#fff",font=("Calibri",20), width=100 ,cursor="hand2",command=choose_file)
    file_button.grid(row=0,column=1,pady=20)

    status_Frame = ctk.CTkFrame(curr_frame,fg_color="#d6ccc2",height=70,corner_radius=0)
    status_Frame.pack(pady=5,expand=True,fill="x")

    status_label = ctk.CTkLabel(status_Frame, text="Not Started",text_color="#555",font=("Calibri",20,"bold"),wraplength=470,textvariable=status_str)
    status_label.pack(anchor="w",padx=20)

    pro_bar = ctk.CTkProgressBar(status_Frame,width=500, height=20,variable=progress)
    pro_bar.pack(anchor="w",padx=17)

def switch_screen(new_screen):
    curr_frame.destroy()
    new_screen()
    
login_screen()
root.mainloop()