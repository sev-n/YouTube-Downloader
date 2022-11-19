from tkinter import messagebox
from pytube import YouTube, request
import pytube.exceptions as exceptions
import app
import socket
import os


class Downloader:
    def __init__(self, url: str, path: str) -> None:
        self.url: str = url
        self.path: str = path
    
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
                            # TODO: Waiting
                            update_text = f"    Downloading {downloaded_bytes} bytes / {round(file_size, 2)} mb -{text}" 
                        else:
                            app.textbox.configure(state="normal")
                            app.textbox.insert("end", f"[MP4] Downloaded - {title}\n")
                            app.textbox.configure(state="disabled")
                            break
    # TODO: Need to review
    def download_audio(self) -> None:
        try:
            youtube = YouTube(self.url)
        except exceptions.PytubeError as e:
            print(e)
        else:
            my_audio = youtube.streams.get_audio_only()
            new_name = f"{my_audio.title}.mp3"
            my_audio.download(filename=new_name, output_path=self.path)
            app.textbox.configure(state="normal")
            app.textbox.insert("end", f"[MP3] Downloaded - {youtube.title}\n")
            app.textbox.configure(state="disabled")