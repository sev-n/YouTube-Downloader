# from tkinter import *
# from tkinter import filedialog, messagebox
import customtkinter as ctk
import downloader
import threading

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Youtube Downloader")
        #self.geometry("870x420")

        
        self.create_widgets()
    
    def create_widgets(self):
        global frame1
        frame1 = ctk.CTkFrame(self, corner_radius=10)
        frame1.grid(row=0, column=0, padx=30, pady=30)
        
        yt_label = ctk.CTkLabel(frame1, text="Paste YouTube link")
        yt_label.grid(row=0, column=0, padx=10, pady=10)
        
        yt_entry = ctk.CTkEntry(frame1, placeholder_text="Enter a link", width=200)
        yt_entry.grid(row=0, column=1, padx=10, pady=10)

    def run(self):
        self.mainloop()
