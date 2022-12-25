from tkinter import filedialog
import customtkinter as ctk
import downloader
import threading

ctk.set_appearance_mode("light") # default appearance mode
#ctk.set_default_color_theme("blue") # default theme

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Youtube Downloader")
        self.resizable(0, 0)
        self.geometry("700x500")
        self.radio_variable: int = ctk.IntVar(value=0)
        self.switch_variable: int = ctk.IntVar(value=0)
        self.path: str = ""

        self.create_widgets() # create all widgets
        
    def create_frame(self):
        global frame1, frame2, frame3, frame4
        frame1 = ctk.CTkFrame(self, corner_radius=15, border_width=1)
        frame1.grid(row=0, column=0, padx=30, pady=(30, 0), sticky="nw")
        
        frame2 = ctk.CTkFrame(self, corner_radius=15, border_width=1)
        frame2.grid(row=1, column=0, padx=30, pady=(20, 0), sticky="nw")

        frame3 = ctk.CTkFrame(self, corner_radius=15, border_width=1)
        frame3.grid(row=2, column=0, padx=30, pady=(20, 0), sticky="nw")
        
        frame4 = ctk.CTkFrame(self, corner_radius=15, border_width=1)
        frame4.grid(row=3, column=0, padx=30, pady=(20, 0), sticky="nw")
    
    def create_label(self):
        global yt_path_detail
        yt_label = ctk.CTkLabel(frame1, text="Paste YouTube link")
        yt_label.grid(row=0, column=0, padx=10, pady=10, ipady=5)
        
        yt_path_detail = ctk.CTkLabel(frame3, text="", width=291)
        yt_path_detail.grid(row=0, column=1, padx=10, pady=10)
    
    def create_entry(self):
        global yt_entry
        yt_entry = ctk.CTkEntry(frame1, placeholder_text="Enter a link", 
                                width=310, 
                                border_width=1)
        yt_entry.grid(row=0, column=1, padx=10, pady=10, ipady=5)
        
    def create_button(self):
        global yt_button, yt_rbutton1, yt_rbutton2
        yt_button = ctk.CTkButton(frame1, text="Download", 
                                  state="disabled",
                                  border_width=1,
                                  fg_color=None,
                                  command=self.download_button_event)
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
        
        yt_button_dialog = ctk.CTkButton(frame3, text="Select Download Path",
                                  border_width=1,
                                  fg_color=None,
                                  command=self.open_file_dialog)
        yt_button_dialog.grid(row=0, column=0, padx=10, pady=10)
    
    def create_switch(self):
        global yt_switch
        yt_switch = ctk.CTkSwitch(frame2, text="Dark mode", 
                                  variable=self.switch_variable, 
                                  onvalue=1,
                                  offvalue=0,
                                  command=self.switch_event)
        yt_switch.grid(row=0, column=0, padx=10, pady=10)
        
    def create_text_box(self):
        global textbox
        textbox = ctk.CTkTextbox(frame4, width=610, cursor='arrow', wrap='word', state="disabled")
        textbox.grid(row=0, column=0, rowspan=2, padx=20, pady=20, sticky="nsew")
        
    def download_button_event(self):
        # https://www.youtube.com/watch?v=4OVCGNmsBwA
        # https://www.youtube.com/watch?v=8RpjwsZGELg
        # https://www.youtube.com/watch?v=SNnSXEpMvv4
        # https://www.youtube.com/watch?v=jfKfPfyJRdk <- live video
        url = yt_entry.get()
        
        dl = downloader.Downloader(url, self.path)

        if self.radio_variable.get() == 1:
            # !Alert: Runtime error occured.
            threading.Thread(target=dl.download_video).start()
            
        elif self.radio_variable.get() == 2:
            threading.Thread(target=dl.download_audio).start()
    
    def rbutton_event(self):
        if self.radio_variable.get() == 1 or self.radio_variable.get() == 2:
            if self.path:
                yt_button.configure(state="normal")
        
    def switch_event(self):
        if self.switch_variable.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
        
    def open_file_dialog(self):
        file_path = filedialog.askdirectory()
        self.path = file_path
        yt_path_detail.configure(text=self.path)
        
        if self.path:
            if self.radio_variable.get() == 1 or self.radio_variable.get() == 2:
                yt_button.configure(state="normal")
        else:
            yt_button.configure(state="disabled")
    
    def create_widgets(self):
        self.create_frame()
        self.create_label()
        self.create_entry()
        self.create_button()
        self.create_switch()
        self.create_text_box()
    
    def run(self):
        self.mainloop()