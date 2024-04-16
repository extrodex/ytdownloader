#import
import tkinter
import customtkinter
from pytube import YouTube
def startDownloadmp4():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        video=ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("Link invalid")
    print("Download Complete")
from pytube import YouTube

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader")

#UI
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()
#finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#download button
downloadmp4 = customtkinter.CTkButton(app, text="Donwload Mp4", command=startDownloadmp4)
downloadmp4.pack()

#Run app
app.mainloop()