import tkinter as tk
from tkinter import filedialog
import object_tracker
import os
import numpy as np
import cv2

input_video = ''
output_video = ''
logs_path = ''
output_video_full_path = ''
logs_full_path = ''

def run():
    if input_video != '' and output_video != '' and logs_path != '' :
        global output_video_full_path
        global logs_full_path
        results = object_tracker.run(input_video, output_video, logs_path)
        logs_full_path = results[0]
        output_video_full_path = results[1]

def choose_file():
    filename = filedialog.askopenfilename(initialdir='./', title="Select File",
                                          filetypes=(
                                              ("All Media Files", ".mp4"),
                                              ("All Media Files", ".flv"),
                                              ("All Media Files", ".avi")))
    if filename:
        # files.append(filename)
        global input_video
        input_video = filename
        label = tk.Label(root, text=input_video, bg='gray')
        label.pack()
        print(filename)


def choose_folder_logs():
    global output_video
    output_video = filedialog.askdirectory()


def choose_folder_video():
    global logs_path
    logs_path = filedialog.askdirectory()

def show_logs():
    global logs_full_path
    if logs_full_path != '':
        os.system("notepad "+logs_full_path)

def play_video():
    global output_video_full_path
    if output_video_full_path == '':
        return
    else:
        cap = cv2.VideoCapture(output_video_full_path)
        if (cap.isOpened() == False):
            print("Error opening video  file")
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(15) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

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

show_logs = tk.Button(root, text="Show Logs", padx=10,
                      pady=5, fg='white', bg='#263D42', command=show_logs)
show_logs.pack()

show_output_video = tk.Button(root, text="Show Video", padx=10,
                      pady=5, fg='white', bg='#263D42', command=play_video)
show_output_video.pack()

root.mainloop()
