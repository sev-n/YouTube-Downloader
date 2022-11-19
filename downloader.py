from tkinter import DISABLED, END, NORMAL, messagebox
from pytube import YouTube, request
import pytube.exceptions as exceptions
import app
import socket
import os

#count = 0

class Downloader:
    def __init__(self, url: str, path: str) -> None: # count: int = 0
        self.url: str = url
        self.path: str = path
        #self.youtube = YouTube(self.url)
    
    def check_connection(self):
        try:
            socket.create_connection(("www.google.com", 80))
        except OSError:
            return False
        return True

    
    # def on_progress(self, stream, chunk, bytes_remaining):
    #     total_size = stream.filesize
    #     bytes_downloaded = total_size - bytes_remaining
    #     percentage_of_completion = bytes_downloaded / total_size * 100
    #     percent = int(percentage_of_completion)
    #     print(bytes_downloaded)
        
        #app.download_list.insert(END, str(self.downloaded))
        
    
    # TODO: Try to change download method -> from sample.py
    def download_video(self) -> None:
        
        global run
        
        try:
            youtube = YouTube(self.url)
        except exceptions.PytubeError as e:
            print(e)
        else:
            #self.youtube.register_on_progress_callback(self.on_progress)
            
            my_video = youtube.streams.get_highest_resolution()
            file_size: int = my_video.filesize * 0.000001 # convert bytes to MB
            title: str = youtube.title
            text = f"   {title}"
            abs_path = f"{self.path}/{my_video.default_filename}"
            
            run = True
            
            if os.path.isfile(abs_path) and os.path.getsize(abs_path) == my_video.filesize:
                    messagebox.showinfo(title="File Exist!", message="Already downloaded file")
                    run = False
            else:
                with open(abs_path, "wb") as file:
                    stream = request.stream(my_video.url)
                    downloaded_bytes: int = 0
                    update_text: str = ""

                    while run:
                        if self.check_connection() == False:
                            continue
                        chunk = next(stream, None)
                        if chunk:
                            file.write(chunk)
                            downloaded_bytes += len(chunk)
                            # TODO: Find bug, not displaying text with multiple downloads
                            update_text = f"    Downloading {downloaded_bytes} bytes / {round(file_size, 2)} mb -{text}"   
                        else:
                            break
            
    def download_audio(self) -> None:
        try:
            youtube = YouTube(self.url)
        except exceptions.PytubeError:
            print(f"Audio file of {youtube.title} is unavailable")
        else:
            my_audio = youtube.streams.get_audio_only()
            new_name = f"{my_audio.title}.mp3"
            my_audio.download(filename=new_name, output_path=self.path)
            # app.status.config(text="Status: Download Completed. 1") # not printing
            print(self.path + youtube.title)

    





# <---------------------------------------------------------------->

# if self.check_connection() == False:
#                 app.download_list.delete(END)
#                 app.download_list.insert(END, "Connection Error, waiting...")
#                 continue
                    
#             if os.path.isfile(abs_path):
#                 # TODO: check if we need to minus the count bcause its not downloading.
#                 print("TRUE") 
#                 app.download_list.delete(END)
#                 app.download_list.insert(END, f"FILE ALREADY DOWNLOADED - {my_video.title}")
#                 app.btn_download_vid.config(state=NORMAL)
                
#             else:
#                 my_video.download(self.path) # skip if file already exist
#                 app.btn_download_vid.config(state=NORMAL)
            
#                 print("Downloaded.")
#                 # print(abs_path)
#                 # print(my_video.title)
#                 # print(my_video.default_filename)
#                 # TODO: we need a way to keep track of index number; -
#                 # todo: so once we insert inside listbox it doesn't always delete the last item.
#                 # app.download_list.delete(END)
#                 # app.download_list.insert(END, f"Downloaded... {youtube.title}")
#                 print(count)