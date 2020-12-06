import tkinter as tk
from tkinter import filedialog
import object_tracker
import os


input_video = ''
output_video = ''
logs_path = ''
output_video_full_path = ''
logs_full_path = ''


def run():
    if input_video != '' and output_video != '' and logs_path != '':
        global output_video_full_path
        global logs_full_path
        results = object_tracker.run(input_video, output_video, logs_path)
        logs_full_path = results[0]
        output_video_full_path = results[1]
        if results:
            show_output_video.config(bg='green')
            show_logs.config(bg='green')
        else:
            show_output_video.config(bg='red')
            show_logs.config(bg='red')


def choose_file():
    filename = filedialog.askopenfilename(initialdir='./', title="Select File",
                                          filetypes=(
                                              ("All Media Files", ".mp4"),
                                              ("All Media Files", ".flv"),
                                              ("All Media Files", ".avi")))
    if filename:
        open_file.config(bg='green')
        # files.append(filename)
        global input_video
        input_video = filename
        label = tk.Label(root, text=input_video, bg='gray')
        label.pack()
        print(filename)


def choose_folder_logs():
    global logs_path
    logs_path = filedialog.askdirectory()
    if logs_path:
        open_logs.config(bg='green')
    else:
        open_logs.config(bg='red')


def choose_folder_video():
    global output_video
    output_video = filedialog.askdirectory()
    if output_video:
        open_movie.config(bg='green')
    else:
        open_movie.config(bg='red')

def show_logs():
    show_output_video.config(bg='red')
    global logs_full_path
    if logs_full_path != '':
        os.system("notepad " + logs_full_path)
        show_output_video.config(bg='green')


def play_video():
    show_logs.config(bg='red')
    global output_video_full_path
    if output_video_full_path != '':
        replaced_path = output_video_full_path.replace("/", "\\")
        os.system("vlc " + replaced_path)
        show_logs.config(bg='green')


root = tk.Tk()
root.resizable(False, False)
# canvas = tk.Canvas(root, height=100, width=100, bg='#263D42')
# canvas.pack()
BUTTON_HEIGHT = 2
BUTTON_WIDTH = 19

open_file = tk.Button(root, text="Choose File", padx=10,
                      pady=5, fg='white', bg='#263D42', command=choose_file)
open_file.config(height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
open_file.pack()

open_movie = tk.Button(root, text="Choose movie directory", padx=10,
                       pady=5, fg='white', bg='#263D42', command=choose_folder_video)
open_movie.config(height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
open_movie.pack()

open_logs = tk.Button(root, text="Choose logs directory", padx=10,
                      pady=5, fg='white', bg='#263D42', command=choose_folder_logs)
open_logs.config(height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
open_logs.pack()

run_app = tk.Button(root, text="Run", padx=10,
                    pady=5, fg='white', bg='#263D42', command=run)
run_app.config(height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
run_app.pack()

show_logs = tk.Button(root, text="Show Logs", padx=10,
                      pady=5, fg='white', bg='#263D42', command=show_logs)
show_logs.config(height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
show_logs.pack()

show_output_video = tk.Button(root, text="Show Video", padx=10,
                              pady=5, fg='white', bg='#263D42', command=play_video)
show_output_video.config(height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
show_output_video.pack()

root.mainloop()
