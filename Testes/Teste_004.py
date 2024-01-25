import tkinter as tk
from tkinter import ttk
from threading import Thread
from urllib.request import urlretrieve, urlcleanup


def download():
    url = "https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe"
    urlretrieve(url, "python-3.10.6-amd64.exe", download_status)
    urlcleanup()


def download_button_clicked():
    # Download the file in a new thread.
    Thread(target=download).start()


def download_status(count, data_size, total_data):
    """
    This function is called by urlretrieve() every time
    a chunk of data is downloaded.
    """
    if count == 0:
        # Set the maximum value for the progress bar.
        progressbar.configure(maximum=total_data)
    else:
        # Increase the progress.
        progressbar.step(data_size)


root = tk.Tk()
root.title("Download File with Progress in Tk")
progressbar = ttk.Progressbar()
progressbar.place(x=30, y=60, width=200)
download_button = ttk.Button(text="Download", command=download_button_clicked)
download_button.place(x=30, y=20)
root.geometry("300x200")
root.mainloop()