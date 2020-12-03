import tkinter as tk
from tkinter import filedialog
import object_tracker

file = ''
movie_path = ''
logs_path = ''

def run():
    if file != '' and movie_path != '' and logs_path != '' :
        object_tracker.run(file, movie_path, logs_path)

def choose_file():
    filename = filedialog.askopenfilename(initialdir='./', title="Select File",
                                          filetypes=(
                                              ("All Media Files", ".mp4"),
                                              ("All Media Files", ".flv"),
                                              ("All Media Files", ".avi")))
    if filename:
        # files.append(filename)
        global file
        file = filename
        label = tk.Label(root, text=file, bg='gray')
        label.pack()
        print(filename)


def choose_folder_logs():
    global movie_path
    movie_path = filedialog.askdirectory()


def choose_folder_video():
    global logs_path
    logs_path = filedialog.askdirectory()

root = tk.Tk()
canvas = tk.Canvas(root, height=100, width=100, bg='#263D42')
canvas.pack()

open_file = tk.Button(root, text="Choose File", padx=10,
                      pady=5, fg='white', bg='#263D42', command=choose_file)
open_file.pack()

open_movie = tk.Button(root, text="Choose movie directory", padx=10,
                      pady=5, fg='white', bg='#263D42', command=choose_folder_video)
open_movie.pack()

open_logs = tk.Button(root, text="Choose logs directory", padx=10,
                      pady=5, fg='white', bg='#263D42', command=choose_folder_logs)
open_logs.pack()

run_app = tk.Button(root, text="Run", padx=10,
                      pady=5, fg='white', bg='#263D42', command=run)
run_app.pack()

root.mainloop()
