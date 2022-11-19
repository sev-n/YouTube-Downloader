# from tkinter import *
# from tkinter import filedialog, messagebox
import tkinter
import customtkinter as ctk
import downloader
import threading

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Youtube Downloader")
        self.resizable(0, 0)
        self.geometry("700x420")
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(0, weight=1)
        self.radio_variable: int = ctk.IntVar(value=0)
        self.switch_variable: str = ctk.IntVar(value=0)

        
        self.create_widgets()     
        
    def create_frame(self):
        global frame1, frame2
        frame1 = ctk.CTkFrame(self, corner_radius=15)
        frame1.grid(row=0, column=0, padx=30, pady=(30, 0), sticky="nw")
        
        frame2 = ctk.CTkFrame(self, corner_radius=15)
        frame2.grid(row=1, column=0, padx=30, pady=(10, 30), sticky="nw")
    
    def create_label(self):
        yt_label = ctk.CTkLabel(frame1, text="Paste YouTube link")
        yt_label.grid(row=0, column=0, padx=10, pady=10, ipady=5)
    
    def create_entry(self):
        yt_entry = ctk.CTkEntry(frame1, placeholder_text="Enter a link", width=300)
        yt_entry.grid(row=0, column=1, padx=10, pady=10, ipady=5)
        
    def create_button(self):
        yt_button = ctk.CTkButton(frame1, text="Download", state="disabled")
        yt_button.grid(row=0, column=2, padx=10, pady=10, ipady=5)
        
        yt_rbutton1 = ctk.CTkRadioButton(frame2, text="MP4", 
                                         variable=self.radio_variable, 
                                         value=1,
                                         command=self.rbutton_event)
        yt_rbutton1.grid(row=0, column=1, padx=(44, 10), pady=10)
        
        yt_rbutton2 = ctk.CTkRadioButton(frame2, text="MP3", 
                                         variable=self.radio_variable, 
                                         value=2,
                                         command=self.rbutton_event)
        yt_rbutton2.grid(row=0, column=2, padx=10, pady=10)
    
    def create_switch(self):
        global yt_switch
        yt_switch = ctk.CTkSwitch(frame2, text="Dark mode", 
                                  variable=self.switch_variable, 
                                  onvalue=1,
                                  offvalue=0,
                                  command=self.switch_event)
        yt_switch.grid(row=0, column=0, padx=10, pady=10)
    
    def rbutton_event(self):
        print(f"Radio button clicked {self.radio_variable.get()}")
        
    def switch_event(self):
        if self.switch_variable.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
        
    
    
    def create_widgets(self):
        self.create_frame()
        self.create_label()
        self.create_entry()
        self.create_button()
        self.create_switch()
    
    def run(self):
        self.mainloop()
        
