from pytube import YouTube
import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def startDownload():
    yt = YouTube(link.get(), on_progress_callback=onProgress)
    if yt:
        stream = yt.streams.get_by_itag(22)
        title.configure(text=yt.title)
        if stream:
            stream.download()
            finishLabel.configure(text="Downloaded")
        else:
            finishLabel.configure(
                text="Stream does not exist", text_color="red")


def onProgress(stream, chunk, bytes_remaning):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaning
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progressPercentage.configure(text=per + '%')
    progressPercentage.update()
    progressBar.set(float(percentage_of_completion) / 100)


app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack()

# progress
progressPercentage = customtkinter.CTkLabel(app, text="0%")
progressPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

app.mainloop()
