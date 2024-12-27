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

    self.current_book_name=None
    self.current_user_name=None
    self.current_table=None
    
    # ------------------------------------------------UI Configuration---------------------------------------------------------
    
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


    # -----------------------------------------------Image configuration on left side-----------------------------------------------
    self.frontimglabel = ct.CTkLabel(self.frontimgframe,text="")
    self.frontimglabel.pack(padx=20, pady=10)

    image = Image.open("img/book1.jpg")

    ctk_image = ct.CTkImage(light_image=image, size=(575,575))
    
    self.frontimglabel.configure(image=ctk_image)
    self.frontimglabel.image = ctk_image

    
    # -----------------------------------------------Login field configuration on right side-----------------------------------------------
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

# --------------------------------------------------------Register field configuration----------------------------------------------------------------------
    
    
    self.titlelabel = ct.CTkLabel(self.frontregframe, text="Register User", fg_color="transparent",
                                      text_color="white", font=("arial black", 32))
    self.titlelabel.grid(row=0,column=3,padx=20, pady=20)

    self.regnametextlabel = ct.CTkLabel(self.frontregframe,text="Full Name   : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.regnametextlabel.grid(row=1,column=2,padx=20, pady=20, sticky="w")

    self.regnameentrylabel = ct.CTkEntry(self.frontregframe,placeholder_text="Enter Your Name",justify="center",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
    self.regnameentrylabel.grid(row=1,column=3,padx=20, pady=20)

    self.regmailtextlabel = ct.CTkLabel(self.frontregframe,text="Email Id   : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.regmailtextlabel.grid(row=2,column=2,padx=20, pady=20, sticky="w")

    self.regmailentrylabel = ct.CTkEntry(self.frontregframe,placeholder_text="Enter Your Email ID",justify="center",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
    self.regmailentrylabel.grid(row=2,column=3,padx=20, pady=20)

    self.regusertextlabel = ct.CTkLabel(self.frontregframe,text="User Id   : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.regusertextlabel.grid(row=3,column=2,padx=20, pady=20, sticky="w")

    self.reguserentrylabel = ct.CTkEntry(self.frontregframe,placeholder_text="Enter Your User ID",justify="center",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
    self.reguserentrylabel.grid(row=3,column=3,padx=20, pady=20)
    
    self.regpasstextlabel = ct.CTkLabel(self.frontregframe,text="Password    : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.regpasstextlabel.grid(row=4,column=2,padx=20, pady=20, sticky="w")

    self.regpassentrylabel = ct.CTkEntry(self.frontregframe,placeholder_text="Enter Your Password",justify="center",show="*",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
    self.regpassentrylabel.grid(row=4,column=3,padx=20, pady=20)
    
    self.regeyeButton = ct.CTkButton(self.frontregframe,image=self.eye_open,corner_radius=20, compound="left",text="",width=40,height=40, command=self.show_password)
    self.regeyeButton.grid(row=4,column=4,padx=20, pady=20)
    

    img = Image.open("img/submit.png")
    self.subbtnimg = ct.CTkImage(light_image=img, dark_image=img, size=(180, 40))  
    
    self.regSub_button = ct.CTkButton(self.frontregframe,text="", hover_color="#3d3d3d",image=self.subbtnimg,corner_radius=1000,bg_color="transparent",fg_color="transparent", width=180, height=40 ,compound="left", command=self.newRegister)
    self.regSub_button.grid(row=6,column=3,padx=20, pady=20)
    
    self.reglog_button = ct.CTkButton(self.frontregframe,text="", hover_color="#3d3d3d",image=self.logbtnimg,corner_radius=1000,bg_color="transparent",fg_color="transparent", width=180, height=40 ,compound="left", command=self.backto_login)
    self.reglog_button.grid(row=7,column=3,padx=20, pady=20)

# ------------------------------------------------------------------------------------------------------------------------------

  def show_password(self):
        if self.password_visible:

            self.frontentrylabel2.configure(show="*")
            self.regpassentrylabel.configure(show="*")
            self.password_visible=False
            self.eyeButton.configure(image=self.eye_open)
            self.regeyeButton.configure(image=self.eye_open)
        
        else:
            self.frontentrylabel2.configure(show="")
            self.regpassentrylabel.configure(show="")
            self.password_visible=True
            self.eyeButton.configure(image=self.eye_closed)
            self.regeyeButton.configure(image=self.eye_closed)
          
# ------------------------------------------------------------------------------------------------------------------------------

  def login(self):
        print("login button clicked")
        if self.frontentrylabel1.get()== '' or self.frontentrylabel2.get() == '':
            messagebox.showwarning("Input Error","Enter UserID and Password")
        
        else:
            try:
                result = ab.findUser(self.frontentrylabel1.get(),self.frontentrylabel2.get())

                if result is not None:

                    self.current_user_name = result[0]
                    self.current_table = self.current_user_name.strip().replace(" ","").lower()
                    messagebox.showinfo("Login Successful",f"Welcome  {result[0]}")
                    self.changeScreen()

                else:
                    messagebox.showerror("Login Error","Invalid UserId or Password")

            except Exception as e:
                print(e)

# ------------------------------------------------------------------------------------------------------------------------------

  def register(self):
    print("register button clicked")

    self.frontlogframe.grid_forget()
    self.frontregframe.grid_configure(row=2, column=1, pady=20, padx=20, sticky="nsew")

  def newRegister(self):
        if self.regnameentrylabel.get()== '' or self.regmailentrylabel.get() == '' or self.reguserentrylabel.get()== '' or self.regpassentrylabel.get()== '' :
            messagebox.showwarning("Input Error","All fields are required.")
        
        else:
            try:
                ab.create_user(self.regnameentrylabel.get(),self.regmailentrylabel.get(),self.reguserentrylabel.get() ,self.regpassentrylabel.get())

                messagebox.showinfo("Successfull", f"You have successfully registered as {self.regnameentrylabel.get()}")
               
                self.regnameentrylabel.delete(0, ct.END)
                self.regmailentrylabel.delete(0, ct.END)
                self.reguserentrylabel.delete(0, ct.END)
                self.regpassentrylabel.delete(0, ct.END)

                self.backto_login()
                    
            except Exception as e:
                print(e)
  
# ------------------------------------------------------------------------------------------------------------------------------
 
  def backto_login(self):
    self.frontregframe.grid_forget()
    self.frontlogframe.grid_configure(row=2, column=1, pady=20, padx=20, sticky="nsew")    
 
  
# ------------------------------------------------------------------------------------------------------------------------------
 
  def changeScreen(self):
    print("Login Successfully")

    self.apptitlelabel.configure(text="Dashboard")

    self.frontimgframe.grid_forget()
    self.frontlogframe.grid_forget()
    self.frontentrylabel1.delete(0, ct.END)
    self.frontentrylabel2.delete(0, ct.END)
    
    
    self.dashboardframe = ct.CTkFrame(self.main_frame, width=1200, height=700, fg_color="transparent")
    self.dashboardframe.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")
    
    self.emptyframe1 = ct.CTkFrame(self.dashboardframe, width=1250, height=50, fg_color="transparent")
    self.emptyframe1.grid(row=0, column=0, columnspan=9, pady=20, padx=20, sticky="nsew")

    img = Image.open("img/logout.png")
    self.loutbtnimg = ctk_image = ct.CTkImage(light_image=img, dark_image=img, size=(120, 30))  

    self.logout_button = ct.CTkButton(self.dashboardframe,text="", hover_color="#3d3d3d",image=self.loutbtnimg,corner_radius=1000,bg_color="transparent",fg_color="transparent", width=120, height=30 ,compound="left", command=self.logout)
    self.logout_button.grid(row=0, column=10, padx=20, pady=20, sticky="ne")
    
    self.dashUser = ct.CTkLabel(self.dashboardframe,text=f"Hello {self.current_user_name}!",width=250,height=60,text_color="white",bg_color="transparent",font=("Verdana", 20,"bold"))
    self.dashUser.grid(row=0,column=0,padx=20, pady=20)
    
    self.newbook = ct.CTkButton(self.dashboardframe,text="Read New Book",width=250,height=60,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"), command=self.readbook)
    self.newbook.grid(row=4,column=3,padx=20, pady=20)

    self.existingbook = ct.CTkButton(self.dashboardframe,text="Read Existing Book",width=250,height=60,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"), command=self.read_existingBook)
    self.existingbook.grid(row=4,column=4,padx=20, pady=20)

    self.emptyframe2 = ct.CTkFrame(self.dashboardframe, width=1250, height=50, fg_color="transparent")
    self.emptyframe2.grid(row=5, column=0, columnspan=9, pady=20, padx=20, sticky="nsew")

    self.booklist = ct.CTkButton(self.dashboardframe,text="My Book List",width=250,height=60,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"), command=self.show_book_list)
    self.booklist.grid(row=6,column=3,padx=20, pady=20)

    self.showanalysis = ct.CTkButton(self.dashboardframe,text="Show Analysis",width=250,height=60,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"))
    self.showanalysis.grid(row=6,column=4,padx=20, pady=20)
    
    self.emptyframe3 = ct.CTkFrame(self.dashboardframe, width=1250, height=50, fg_color="transparent")
    self.emptyframe3.grid(row=7, column=0, columnspan=9, pady=20, padx=20, sticky="nsew")

    self.oldbook = ct.CTkButton(self.dashboardframe,text="Add Old Book",width=250,height=60,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"), command=self.addoldbook)
    self.oldbook.grid(row=8,column=3, columnspan=2,padx=20, pady=20)

  def logout(self):
    self.apptitlelabel.configure(text="Book Data")
    self.dashboardframe.grid_forget()

    self.frontimgframe.grid_configure(row=1, column=0, pady=20, padx=20, sticky="nsew")
    self.frontlogframe.grid_configure(row=1, column=1, pady=20, padx=20, sticky="nsew")

    self.current_book_name=None
    self.current_user_name=None
    self.current_table=None

  def readbook(self):
    pass
    
  def read_existingBook(self):
    pass
    
  def show_book_list(pass):
    pass
    
  def show_book_analysis(self):
    pass
    
  def addoldbook(self):
    pass



# -----------------------------------------------------Main function to run the app-----------------------------------------------------

if __name__ == "__main__":
  app = App()
  app.mainloop()
