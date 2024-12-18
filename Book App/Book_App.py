# Import required libraries

import pandas as pd
import pandastable as pdtable
import customtkinter as ct
import tkinter as tk
from tkinter import messagebox, filedialog
import cv2
from PIL import Image, ImageTK
from datetime import datetime
import Connect_DB as connection


# Setting up database connection 

db = connection.DB_connect()

# App appearance
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

# App Code

class App(ct.CTk):

  def __init__(self):
    super().__init()

    self.title("Book Data App")
    self.geometry("1400x850")

    # Main frame for the app
    self.main_frame = ct.CTkScrollableFrame(self)
    self.main_frame.pack(fill='both', expand=True)

    # Title Frame
    self.titlelabelframe = ct.CTkFrame(self.main_frame, width=600, height=100, fg_color="transparent")
    self.titlelabelframe.grid(row=0, column=0, columnspan=10,pady=20, padx=20)  

    self.apptitlelabel = ct.CTkLabel(self.titlelabelframe, text="Book Data", fg_color="transparent",
                                  text_color="white", font=("arial black", 32))
    self.apptitlelabel.pack()  

    # ---------------------------------------------------------------------------------------------------------
    
    # Front image frame (on the left side)
    self.frontimgframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    self.frontimgframe.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")  

    # Front login frame (on the right side)
    self.frontlogframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    self.frontlogframe.grid(row=2, column=1, pady=20, padx=20, sticky="nsew")

    # Front register frame (on the right side)
    self.frontregframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")

    # ---------------------------------------------------------------------------------------------------------


# Main function to run the app

if __name__ == "__main__":
  app = App()
  app.mainloop()
