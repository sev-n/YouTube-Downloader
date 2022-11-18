# from tkinter import *
# from tkinter import filedialog, messagebox
import customtkinter as ctk
import downloader
import threading

ctk.set_appearance_mode("light")

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Youtube Downloader")
        self.geometry("870x420")
        self.path: str = ""

        
        self.create_frame()
    
    def create_frame(self):
        frame1 = ctk.CTkFrame(self)
        frame1.grid(row=0, column=0)
        
        frame2 = ctk.CTkFrame(self)
        frame2.grid(row=1, column=1)



    def run(self):
        self.mainloop()
