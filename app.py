import tkinter as tk
from tkinter import filedialog
import object_tracker

files = []

def run():
    print(files[0])
    if files[0]:
        object_tracker.run(files[0])

def choose_file():
    filename = filedialog.askopenfilename(initialdir='/', title="Select File",
                                          filetypes=(
                                              ("All Media Files", ".mp4"),
                                              ("All Media Files", ".flv"),
                                              ("All Media Files", ".avi")))
    if filename:
        files.append(filename)
        label = tk.Label(root, text=files[0], bg='gray')
        label.pack()
        print(filename)


root = tk.Tk()
canvas = tk.Canvas(root, height=100, width=100, bg='#263D42')
canvas.pack()

open_file = tk.Button(root, text="Choose File", padx=10,
                      pady=5, fg='white', bg='#263D42', command=choose_file)
open_file.pack()

run_app = tk.Button(root, text="Run", padx=10,
                      pady=5, fg='white', bg='#263D42', command=run)
run_app.pack()

root.mainloop()
