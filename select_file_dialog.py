import tkinter as tk
from tkinter import filedialog

def select_image_file():
    # Initialize tkinter and hide the main root window
    root = tk.Tk()
    root.withdraw()
    # Open a file chooser dialog and return the file path selected
    file_path = filedialog.askopenfilename(
        title="Select Bridge Structure Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff"), ("All files", "*.*")]
    )
    return file_path
