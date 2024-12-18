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
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_frame.grid_columnconfigure(1, weight=1)
    self.main_frame.grid_rowconfigure(1, weight=1)


    # Image configuration on left side
    self.frontimglabel = ct.CTkLabel(self.frontimgframe,text="")
    self.frontimglabel.pack(padx=20, pady=10)

    image = Image.open("img/book1.jpg")

    ctk_image = ct.CTkImage(light_image=image, size=(575,575))
    
    self.frontimglabel.configure(image=ctk_image)
    self.frontimglabel.image = ctk_image

    
    # Login field configuration on right side
    self.titlelabel = ct.CTkLabel(self.frontlogframe, text="Login User", fg_color="transparent",
                                  text_color="white", font=("arial black", 32))
    self.titlelabel.grid(row=0,column=3,padx=20, pady=20)
           
    self.fronttextlabel1 = ct.CTkLabel(self.frontlogframe,text="User ID    : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.fronttextlabel1.grid(row=1,column=2,padx=20, pady=20)

    self.frontentrylabel1 = ct.CTkEntry(self.frontlogframe,placeholder_text="Enter Your User ID",justify="center",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
    self.frontentrylabel1.grid(row=1,column=3,padx=20, pady=20)

    
    self.fronttextlabel2 = ct.CTkLabel(self.frontlogframe,text="Password    : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.fronttextlabel2.grid(row=2,column=2,padx=20, pady=20)

    self.frontentrylabel2 = ct.CTkEntry(self.frontlogframe,placeholder_text="Enter Your Password",justify="center",show="*",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
    self.frontentrylabel2.grid(row=2,column=3,padx=20, pady=20)
    
    
    img = Image.open("img/open_eye.png")
    self.eye_open = ct.CTkImage(light_image=img, size=(35,30))

    img = Image.open("img/closed_eye.png")
    self.eye_closed = ct.CTkImage(light_image=img, size=(35,30))

    self.eyeButton = ct.CTkButton(self.frontlogframe,image=self.eye_open,corner_radius=20, compound="left",text="",width=40,height=40, command=self.show_password)
    self.eyeButton.grid(row=2,column=4,padx=20, pady=20)
    self.password_visible = False

    img = Image.open("img/login.png")
    self.logbtnimg = ct.CTkImage(light_image=img, dark_image=img, size=(180, 40))  
    
    img = Image.open("img/register.png")
    self.regbtnimg = ct.CTkImage(light_image=img, dark_image=img, size=(180, 40))  
    

    self.login_button = ct.CTkButton(self.frontlogframe,text="", hover_color="#3d3d3d",image=self.logbtnimg,corner_radius=1000,bg_color="transparent",fg_color="transparent", width=180, height=40 ,compound="left", command=self.login)
    self.login_button.grid(row=4,column=3,padx=20, pady=20)

    self.register_button = ct.CTkButton(self.frontlogframe,text="",image=self.regbtnimg,width=180,height=40,corner_radius=1000,bg_color="transparent",fg_color="transparent",hover_color="#3d3d3d",compound="left", command=self.register)
    self.register_button.grid(row=5,column=3,padx=20, pady=20)

# ------------------------------------------------------------------------------------------------------------------------------

def login(self):
    print("login button clicked")

# ------------------------------------------------------------------------------------------------------------------------------

  def register(self):
    print("register button clicked")
    
# ------------------------------------------------------------------------------------------------------------------------------

# Main function to run the app

if __name__ == "__main__":
  app = App()
  app.mainloop()
