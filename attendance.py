from tkinter import *
import os
import subprocess
import sys
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime

class Attends:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Button to open CSV
        bl = Button(
            self.root,
            command=self.open_csv,
            text="View Attendance in Excel",
            font=("Rockwell", 15),
            bg="black",
            fg="white",
            cursor="hand2"
        )
        bl.place(x=180, y=150, width=250, height=50)

    def open_csv(self):
        file_path = "attendance.csv"  # make sure the file exists
        try:
            if sys.platform == "win32":   # Windows
                os.startfile(file_path)
            elif sys.platform == "darwin":  # macOS
                subprocess.call(["open", file_path])
            else:  # Linux
                subprocess.call(["xdg-open", file_path])
        except Exception as e:
            print(f"Error opening file: {e}")

if __name__ == "__main__":
    root = Tk()
    obj= Attends(root)
    root.mainloop()
