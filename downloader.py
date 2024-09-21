#importing libraries and required modules in the code

import pytube
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as font
from pytube import YouTube

#backend code
#code for file location
Folder_Name = ""

def Get_Location():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        Location_error.config(text= Folder_Name , fg="green")
    
    else:
        Location_error.config(text="Choose Folder!", fg="red")


#Download video

def Download_Video():
    choice = downloader_choices.get()
    url = downloader_entry.get()

    if (len(url)>1):
        yt = pytube.YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            downloader_error.config(text="Check the link", fg="red")
    else:
        downloader_error.config(text="")

    

#Download function
    select.download(Folder_Name)
    downloader_error.config(text="Download complete !")




root = Tk()
root.title("YouDown")

#Setting font for button
buttonfont = font.Font(family="Calisto MT")


#Dimension of the window
root.geometry("400x500")
root.columnconfigure(0, weight=1) #to set all contents in center.

#Contents of the app
#Top label heading
downloaderlabel = Label(root, height=4, text= "Enter the URL of the video", font=("castellar",15,"bold"))
downloaderlabel.grid()

#Link entry box
downloader_entryVar =StringVar()
downloader_entry = Entry(root, width = 50, textvariable = downloader_entryVar, cursor="plus")
downloader_entry.place(height=5)
downloader_entry.grid()

#Error msg
downloader_error = Label(root, height=3, text="The link provided is invalid!", fg= "red", font=("Serif", 10, "italic"))
downloader_error.grid()

#Asking where to save file label
save_label = Label(root, height=1, text="Download location", font=("castellar", 15, "bold"))
save_label.grid()

#Button for saving file
save_entry = Button(root, width=10, bg = "orange", fg = "white", text= "Browse", command=Get_Location)
save_entry['font'] = buttonfont
save_entry.grid()

#Location error msg
Location_error = Label(root, height=3, text="Error Msg of path", fg="red", font=("Serif", 10, "italic"))
Location_error.grid()

#Download Quality
downloader_quality = Label(root, text="Select quality", font=("castellar",15,"bold"), height= 2)
downloader_quality.grid()

#Choose quality box
choices =["1080p", "144p", "Audio file"]
downloader_choices = ttk.Combobox(root, height= 20, values=choices)
downloader_choices.grid()

#Download button
downloader_button = Button(root, width=10, bg= "orange", fg="white", text= "Download", command=Download_Video)
downloader_button['font'] = buttonfont
downloader_button.grid()
 



root.mainloop()
