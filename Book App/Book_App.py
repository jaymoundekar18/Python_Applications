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
    
# -----------------------------------------------------
  def logout(self):
    self.apptitlelabel.configure(text="Book Data")
    self.dashboardframe.grid_forget()

    self.frontimgframe.grid_configure(row=1, column=0, pady=20, padx=20, sticky="nsew")
    self.frontlogframe.grid_configure(row=1, column=1, pady=20, padx=20, sticky="nsew")

    self.current_book_name=None
    self.current_user_name=None
    self.current_table=None
# -----------------------------------------------------
  def readbook(self):
    self.apptitlelabel.configure(text="Read New Book")

    self.dashboardframe.grid_forget()

    # Image and GIF Frame (on the left side)
    self.gifimgframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    self.gifimgframe.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")  

    # Book Details Frame (on the right side)
    self.bookdetailsframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    self.bookdetailsframe.grid(row=2, column=1, pady=20, padx=20, sticky="nsew")

    # Book Reading Frame (on the right side)
    self.bookreadframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_frame.grid_columnconfigure(1, weight=1)
    self.main_frame.grid_rowconfigure(1, weight=1)


    # GIF Image configuration on left side

    image = Image.open("img/home.png")

    ctk_image = ct.CTkImage(light_image=image, size=(120,35))

    self.backtodash = ct.CTkButton(self.gifimgframe,text="", hover_color="#3d3d3d",image=ctk_image,corner_radius=1000,bg_color="transparent",fg_color="transparent", width=150, height=40 ,compound="left", command=self.backtodashboard1)
    self.backtodash.pack(padx=20, pady=10, anchor="nw")
    

    self.gifimglabel = ct.CTkLabel(self.gifimgframe,text="")
    self.gifimglabel.pack(padx=20, pady=90)

    image = Image.open("img/read0.png")

    ctk_image = ct.CTkImage(light_image=image, size=(600,400))
    
    self.gifimglabel.configure(image=ctk_image)
    self.gifimglabel.image = ctk_image

    # Book Details configuration on right side
    self.bdetailslabel = ct.CTkLabel(self.bookdetailsframe, text="Book Details", fg_color="transparent",
                                  text_color="white", font=("arial black", 32))
    self.bdetailslabel.grid(row=0,column=3,padx=20, pady=20)

    self.booktitletextlabel = ct.CTkLabel(self.bookdetailsframe,text="Book Title   : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.booktitletextlabel.grid(row=1,column=2,padx=20, pady=20, sticky="w")

    self.booktitleentrylabel = ct.CTkEntry(self.bookdetailsframe,placeholder_text="Enter Your Book Title",justify="center",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
    self.booktitleentrylabel.grid(row=1,column=3,padx=20, pady=20)

    self.bauthortextlabel = ct.CTkLabel(self.bookdetailsframe,text="Author Name   : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.bauthortextlabel.grid(row=2,column=2,padx=20, pady=20, sticky="w")

    self.bauthorentrylabel = ct.CTkEntry(self.bookdetailsframe,placeholder_text="Enter Book Author Name",justify="center",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
    self.bauthorentrylabel.grid(row=2,column=3,padx=20, pady=20)

    self.bookgentextlabel = ct.CTkLabel(self.bookdetailsframe,text="Book Genre   : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.bookgentextlabel.grid(row=3,column=2,padx=20, pady=20, sticky="w")

    book_genres = [
                'Action Fiction', 'Adventure Fiction', 'Alternate History', 'Autobiography', 'Biography', 
                'Contemporary Literature', 'Contemporary Romance', 'Crime Fiction', 'Detective Fiction', 'Essay',
                'Fairy Tale', 'Fantasy', 'Fantasy Fiction', 'Fiction', 'Genre Fiction', 'Graphic Novel', 
                'Historical Fantasy', 'Historical Fiction', 'Historical Romance', 'History',
                'Horror Fiction', 'Humor', 'Literary Fiction', 'Magical Realism', 'Memoir', 'Mystery', 'Narrative', 
                'New Adult Fiction', 'Non-fiction', 'Novel', 'Paranormal Romance', 'Philosophy', 'Poetry', 'Quotation', 
                'Romance', 'Romance Novel', 'Satire', 'Science', 'Science Fantasy', 'Science Fiction',
                'Self-help Book', 'Short Story', 'Social Science', 'Speculative Fiction', 'Spirituality', 'Thriller', 
                'Travel Literature', 'True Crime', 'Western Fiction', "Women's Fiction", 'Young Adult Literature'
                ]

    self.bookgenentrylabel = ct.CTkOptionMenu(self.bookdetailsframe,values=book_genres,width=350,height=50,bg_color="transparent", fg_color="#ebb434",font=("arial", 16),text_color="white")
    self.bookgenentrylabel.grid(row=3,column=3,padx=20, pady=20)
   
    self.bookpgtextlabel = ct.CTkLabel(self.bookdetailsframe,text="Number of Book Pages    : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.bookpgtextlabel.grid(row=4,column=2,padx=20, pady=20, sticky="w")

    self.bookpgentrylabel = ct.CTkEntry(self.bookdetailsframe,placeholder_text="eg. 465 (Note: Numbers only)",justify="center",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
    self.bookpgentrylabel.grid(row=4,column=3,padx=20, pady=20)

    self.bookSub_button = ct.CTkButton(self.bookdetailsframe,text="", hover_color="#3d3d3d",image=self.subbtnimg,corner_radius=1000,bg_color="transparent",fg_color="transparent", width=180, height=40 ,compound="left", command=self.valBookData)
    self.bookSub_button.grid(row=6,column=3,padx=20, pady=40)
    

    # Book Reading configuration on right side
    self.is_running = False
    self.is_existingBook = False
    self.is_newBook = True

    self.booktitleframe = ct.CTkFrame(self.bookreadframe, width=600, height=100, fg_color="transparent")
    self.booktitleframe.grid(row=0, column=0, columnspan=6, pady=20, padx=20, sticky="nsew")

    self.booktitle = ct.CTkLabel(self.booktitleframe, text="", fg_color="transparent",justify="center",
                                  text_color="white", font=("arial black", 32))
    self.booktitle.grid(row=0,column=3,padx=20, pady=20,sticky="nsew") 

    self.booktimerlabel = ct.CTkLabel(self.bookreadframe, text="00:00:00", fg_color="transparent",
                                  text_color="white", font=("Verdana ", 32,"bold"))
    self.booktimerlabel.grid(row=2,column=3,padx=20, pady=20) 

    image = Image.open("img/sandclock.gif")

    self.sandclockimg = ct.CTkImage(light_image=image, size=(100,100))
    

    self.clockimglabel = ct.CTkLabel(self.bookreadframe, text="", image=self.sandclockimg , fg_color="transparent")
    self.clockimglabel.grid(row=3,column=3,padx=20, pady=20)

    self.bookstartbtn = ct.CTkButton(self.bookreadframe,text="Start Timer",width=180,height=50,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"), command=self.start)
    self.bookstartbtn.grid(row=4,column=2,padx=20, pady=20)

    self.bookpausebtn = ct.CTkButton(self.bookreadframe,text="Pause",width=180,height=50,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"),state="disabled", command=self.pausetimer)
    self.bookpausebtn.grid(row=4,column=3,padx=20, pady=20)

    self.bookstopbtn = ct.CTkButton(self.bookreadframe,text="Stop",width=180,height=50,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"),state="disabled", command=self.stoptimer)
    self.bookstopbtn.grid(row=4,column=4,padx=20, pady=20)


# -----------------------------------------------------   
  
  def valBookData(self):
    if self.booktitleentrylabel.get()== '' or self.bauthorentrylabel.get() == '' or self.bookgenentrylabel.get()== '' or self.bookpgentrylabel.get()== '' :
      messagebox.showwarning("Input Error","All fields are required.")
        
    else:
      
      try:
        start_date = datetime.now().strftime("%d/%m/%Y")
        print("new book: "+self.current_table ,self.booktitleentrylabel.get(),self.bauthorentrylabel.get(),self.bookgenentrylabel.get() ,self.bookpgentrylabel.get(),"00:00:00",type(start_date))
        
        ab.save_new_book(self.current_table ,self.booktitleentrylabel.get(),self.bauthorentrylabel.get(),self.bookgenentrylabel.get() ,self.bookpgentrylabel.get(),"00:00:00",start_date)
        
        self.current_book_name = self.booktitleentrylabel.get().title()
        title = "Reading : " + self.current_book_name
        messagebox.showinfo("Successfull","Book Saved Successfully!")

        self.booktitleentrylabel.delete(0, ct.END)
        self.bauthorentrylabel.delete(0, ct.END)
        # self.bookgenentrylabel.delete(0, ct.END)
        self.bookpgentrylabel.delete(0, ct.END)

        
        self.newBook(title)
                    

      except Exception as e:
        print(e)


# -----------------------------------------------------   
  
    def newBook(self,title):
      self.bookdetailsframe.grid_forget()
      self.bookreadframe.grid(row=2, column=1, pady=20, padx=20, sticky="nsew")
      self.booktitle.configure(text=title)
      print("Book Saved")

# -----------------------------------------------------   
  
    def startread(self):
      self.gif_path_1 = "img/sandclock.gif" 
      self.gif_1 = Image.open(self.gif_path_1)
      self.current_frame_1 = 0
      self.frames_1 = self.load_gif_1(self.gif_1)

      self.gif_paths = ["img/read1.gif", "img/read2.gif"]

      self.frames_2 = []
      self.current_gif_index = 0  
      self.load_all_gifs()  
      self.current_frame_2 = 0
      self.is_paused = False
      self.elapsed_time = 0

# -----------------------------------------------------   
  
    def start(self):
      pygame.mixer.music.load(r"C:\Users\jaymo\Downloads\music.mp3")  
      pygame.mixer.music.play(-1)
      if self.is_newBook:
        self.startread()
        self.bookstartbtn.configure(state="disabled")
        self.bookpausebtn.configure(state="normal")
        self.bookstopbtn.configure(state="normal")
        self.is_running=True
        self.update_time()
        self.animate_gif_1()   
        self.animate_gif_2()   

      elif self.is_existingBook:
        self.startread()
        self.bookstartbtn1.configure(state="disabled")
        self.bookpausebtn1.configure(state="normal")
        self.bookstopbtn1.configure(state="normal")
        self.is_running=True
        self.update_time()
        self.animate_gif_1()   
        self.animate_gif_2()   
        
      else:
        pass

# -----------------------------------------------------   
  
    def load_gif_1(self, gif):
      frames = []
      try:
        while True:
          frame = gif.copy()
          frame = frame.resize((150, 150), Image.LANCZOS)
          frames.append(ImageTk.PhotoImage(frame))
          gif.seek(len(frames))  
      except EOFError:
        pass  
        
      return frames 

# -----------------------------------------------------   
  
    def load_gif_2(self, gif):
      frames = []
      try:
        while True:
          frame = gif.copy()
          frame = frame.resize((800, 550), Image.LANCZOS)
          frames.append(ImageTk.PhotoImage(frame))
          gif.seek(len(frames))  
      
      except EOFError:
        pass  
        
      return frames

# -----------------------------------------------------   
  
    def load_all_gifs(self):
      for path in self.gif_paths:
        gif = Image.open(path)
        frames = self.load_gif_2(gif)
        self.frames_2.append(frames)

# -----------------------------------------------------   
      
    def animate_gif_1(self):
      if self.is_newBook:
        if self.frames_1 and self.is_running and not self.is_paused:
          self.clockimglabel.configure(image=self.frames_1[self.current_frame_1])
          self.current_frame_1 = (self.current_frame_1 + 1) % len(self.frames_1)
          self.after(100, self.animate_gif_1)  # Set delay to 1000 milliseconds (1 second)

      elif self.is_existingBook:
        if self.frames_1 and self.is_running and not self.is_paused:
          self.clockimglabel1.configure(image=self.frames_1[self.current_frame_1])
          self.current_frame_1 = (self.current_frame_1 + 1) % len(self.frames_1)
          self.after(100, self.animate_gif_1)  # Set delay to 1000 milliseconds (1 second)

      else:
        pass


# -----------------------------------------------------   
  
    def animate_gif_2(self):
      if self.is_newBook:
        
        if self.frames_2 and self.is_running and not self.is_paused:
          current_frames = self.frames_2[self.current_gif_index]
          self.gifimglabel.configure(image=current_frames[self.current_frame_2])
          self.current_frame_2 = (self.current_frame_2 + 1) % len(current_frames)

                
          if self.current_frame_2 == 0:
            self.current_gif_index = (self.current_gif_index + 1) % len(self.frames_2)  

          self.after(30, self.animate_gif_2) 

      elif self.is_existingBook:
        
        if self.frames_2 and self.is_running and not self.is_paused:
          
          current_frames = self.frames_2[self.current_gif_index]
          self.gifimglabel1.configure(image=current_frames[self.current_frame_2])
          self.current_frame_2 = (self.current_frame_2 + 1) % len(current_frames)

            
          if self.current_frame_2 == 0:  
            self.current_gif_index = (self.current_gif_index + 1) % len(self.frames_2)  

          self.after(30, self.animate_gif_2) 

        else:
            pass        


# -----------------------------------------------------   
  
    def update_time(self):
        if self.is_newBook:
          
          if self.is_running and not self.is_paused:
            self.elapsed_time += 1
            current_time = time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time))
            self.booktimerlabel.configure(text=current_time)
            self.after(1000, self.update_time)

        elif self.is_existingBook:
          if self.is_running and not self.is_paused:
            self.existingTime += 1        
            current_time = time.strftime("%H:%M:%S", time.gmtime(self.existingTime))
            self.booktimerlabel1.configure(text=current_time)
            self.after(1000, self.update_time)
        
        else:
            pass

# -----------------------------------------------------   
  
    def pausetimer(self):
      if self.is_newBook:
        if self.is_running:
          self.is_paused = not self.is_paused  # Toggle pause state
          if self.is_paused:
            pygame.mixer.music.pause()
            self.bookpausebtn.configure(text="Continue")  # Change button text to Continue
                
          else:
            pygame.mixer.music.unpause()
            self.bookpausebtn.configure(text="Pause")  # Change button text to Pause
            self.update_time()
            self.animate_gif_1()
            self.animate_gif_2()

      elif self.is_existingBook:
        if self.is_running: 
          self.is_paused = not self.is_paused  # Toggle pause state
          if self.is_paused:
            pygame.mixer.music.pause()
            self.bookpausebtn1.configure(text="Continue")  # Change button text to Continue
          else:
            pygame.mixer.music.unpause()
            self.bookpausebtn1.configure(text="Pause")  # Change button text to Pause
            self.update_time()
            self.animate_gif_1()
            self.animate_gif_2()
        
      else:
        pass

# -----------------------------------------------------   
  
    def stoptimer(self):

      pygame.mixer.music.stop()
      self.pausetimer()

      result = messagebox.askyesno("Stop Timer", "Are you sure you want to stop the timer?")
        
      if self.is_newBook:
        bookstatus = messagebox.askyesno("Book Status",f"Is {self.current_book_name} book completed ? ")

        if result and bookstatus:
          self.bookstartbtn.configure(state="disabled")
          self.bookpausebtn.configure(state="disabled")
          self.bookstopbtn.configure(state="disabled")
          self.is_running = False 
          self.is_completed = True 

          self.ratingLabel = ct.CTkLabel(self.bookreadframe,text=f"Rate {self.current_book_name} :", fg_color="transparent",
                                      text_color="white", font=("Palatino Linotype", 20))
          self.ratingLabel.grid(row=5,column=2,padx=20, pady=20)

          self.ratingEntry = ct.CTkEntry(self.bookreadframe, placeholder_text="eg. 3.5, 4.0, 5  ",justify="center",width=180,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
          self.ratingEntry.grid(row=5,column=3,padx=20, pady=20)

          self.reviewLabel = ct.CTkLabel(self.bookreadframe,text=f"Write book review :", fg_color="transparent",
                                text_color="white", font=("Palatino Linotype", 20))
          self.reviewLabel.grid(row=6,column=2,padx=20, pady=20)

          self.reviewEntry = ct.CTkTextbox(self.bookreadframe, width=600,height=400,bg_color="#3d3d3d",fg_color="transparent",font=("Palatino Linotype", 16))
          self.reviewEntry.grid(row=7,column=2, columnspan=3,padx=20, pady=20)
          
          self.timesavebtn = ct.CTkButton(self.bookreadframe,text="Save Time",width=180,height=50,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"), command=self.update_dbtime)
          self.timesavebtn.grid(row=8,column=3,padx=20, pady=20)

        elif result:  
          self.bookstartbtn.configure(state="disabled")
          self.bookpausebtn.configure(state="disabled")
          self.bookstopbtn.configure(state="disabled")
          self.is_running = False

          self.timesavebtn = ct.CTkButton(self.bookreadframe,text="Save Time",width=180,height=50,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"), command=self.update_dbtime)
          self.timesavebtn.grid(row=5,column=3,padx=20, pady=20) 

      elif self.is_existingBook:
        bookstatus = messagebox.askyesno("Book Status",f"Is {self.current_book_name} book completed ? ")
        if result and bookstatus:
          self.bookstartbtn1.configure(state="disabled")
          self.bookpausebtn1.configure(state="disabled")
          self.bookstopbtn1.configure(state="disabled")
          self.is_running = False  
          self.is_completed = True 

          self.ratingLabel1 = ct.CTkLabel(self.existingbookframe_2,text=f"Rate {self.current_book_name} :", fg_color="transparent",
                                text_color="white", font=("Palatino Linotype", 20))
          self.ratingLabel1.grid(row=5,column=2,padx=20, pady=20)

          self.ratingEntry1 = ct.CTkEntry(self.existingbookframe_2, placeholder_text="eg. 3.5, 4.0, 5  ",justify="center",width=180,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
          self.ratingEntry1.grid(row=5,column=3,padx=20, pady=20)

          self.reviewLabel1 = ct.CTkLabel(self.existingbookframe_2,text=f"Write book review :", fg_color="transparent",
                                text_color="white", font=("Palatino Linotype", 20))
          self.reviewLabel1.grid(row=6,column=2,padx=20, pady=20)

          self.reviewEntry1 = ct.CTkTextbox(self.existingbookframe_2, width=600,height=400,bg_color="#3d3d3d",fg_color="transparent",font=("Palatino Linotype", 16))
          self.reviewEntry1.grid(row=7,column=2, columnspan=3,padx=20, pady=20)

          self.timesavebtn1 = ct.CTkButton(self.existingbookframe_2,text="Save Time",width=180,height=50,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"), command=self.update_dbtime)
          self.timesavebtn1.grid(row=8,column=3,padx=20, pady=20)

        elif result:
          self.bookstartbtn1.configure(state="disabled")
          self.bookpausebtn1.configure(state="disabled")
          self.bookstopbtn1.configure(state="disabled")
          self.is_running = False  
          
          self.timesavebtn1 = ct.CTkButton(self.existingbookframe_2,text="Save Time",width=180,height=50,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"), command=self.update_dbtime)
          self.timesavebtn1.grid(row=5,column=3,padx=20, pady=20)

        else: 
          pass

      else:
        pass

# -----------------------------------------------------   
  
    def update_dbtime(self):
      if self.is_newBook:
        print("Time updated in db ", self.booktimerlabel.cget("text"))
        btime = self.booktimerlabel.cget("text")

        if self.is_completed:
          end_date = datetime.now().strftime("%d/%m/%Y")
          print(self.current_table, self.current_book_name, btime,self.ratingEntry.get(),self.reviewEntry.get("0.0", "end-1c"),end_date)

          ab.update_book_trr(self.current_table, self.current_book_name, btime,float(self.ratingEntry.get()),self.reviewEntry.get("0.0", "end-1c"), "Completed",end_date)

          messagebox.showinfo("Successfull", "Your reading data is saved!")

        else:
          ab.update_book_time(self.current_table, self.current_book_name, btime, "In Progress")
          messagebox.showinfo("Successfull", "Your reading time is saved!")
            
          self.gifimgframe.grid_forget()
          self.bookdetailsframe.grid_forget()
          self.bookreadframe.grid_forget()
          self.apptitlelabel.configure(text="Dashboard")            
          self.dashboardframe.grid_configure(row=2, column=0, pady=20, padx=20, sticky="nsew")
          self.is_completed=False

      elif self.is_existingBook:
        
        print("Time updated in existing db ", self.booktimerlabel1.cget("text"))
        btime = self.booktimerlabel1.cget("text")
        
        if self.is_completed:
          end_date = datetime.now().strftime("%d/%m/%Y")
          print(self.current_table, self.current_book_name, btime, float(self.ratingEntry1.get()),self.reviewEntry1.get("0.0", "end-1c"),end_date)
          ab.update_book_trr(self.current_table, self.current_book_name, btime, float(self.ratingEntry1.get()),self.reviewEntry1.get("0.0", "end-1c"), "Completed",end_date)
          messagebox.showinfo("Successfull", "Your reading data is saved!")

        else:
          ab.update_book_time(self.current_table, self.current_book_name, btime, "In Progress")
          messagebox.showinfo("Successfull", "Your reading time is saved!")
          
          self.gifimgframe.grid_forget()
          self.existingbookframe_1.grid_forget()
          self.dropdown_frame.grid_forget()
          self.existingbookframe_2.grid_forget()
          self.booktitleframe.grid_forget()
          self.apptitlelabel.configure(text="Dashboard")
          self.dashboardframe.grid_configure(row=2, column=0, pady=20, padx=20, sticky="nsew")
          self.is_completed=False

      else:
          pass
  
# -----------------------------------------------------    
 
  def read_existingBook(self):
    self.apptitlelabel.configure(text="Read Existing Book")

    self.dashboardframe.grid_forget()
    print(self.current_table, self.current_user_name)
    res = ab.findUserBook(self.current_table)

    books=[]
    for book in res:
        books.append(book[0])
    print(books)    
    self.items= books
    self.bsearchVar = ct.StringVar()

    # Image and GIF Frame (on the left side)
    self.gifimgframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    self.gifimgframe.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")  

    
    image = Image.open("img/home.png")
    ctk_image = ct.CTkImage(light_image=image, size=(120,35))
    self.backtodash = ct.CTkButton(self.gifimgframe,text="", hover_color="#3d3d3d",image=ctk_image,corner_radius=1000,bg_color="transparent",fg_color="transparent", width=150, height=40 ,compound="left", command=self.backtodashboard3)
    self.backtodash.pack(padx=20, pady=10, anchor="nw")
    
    self.gifimglabel1 = ct.CTkLabel(self.gifimgframe,text="")
    self.gifimglabel1.pack(padx=20, pady=90)

    image = Image.open("img/read0.png")

    ctk_image = ct.CTkImage(light_image=image, size=(600,400))
    
    self.gifimglabel1.configure(image=ctk_image)
    self.gifimglabel1.image = ctk_image

    # Read Existing Book Frame (on the right side)
    self.existingbookframe_1 = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    self.existingbookframe_1.grid(row=2, column=1, pady=20, padx=20, sticky="nsew")
    
    self.bsearchBox = ct.CTkEntry(self.existingbookframe_1, textvariable=self.bsearchVar,justify="center" , width=400, height=40, fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.bsearchBox.grid(row=0,column=0, columnspan=4,padx=20, pady=20)
    self.bsearchBox.bind("<KeyRelease>", self.update_dropdown)


    self.bsearchBtn = ct.CTkButton(self.existingbookframe_1,text="Search",width=60, height=40,corner_radius=10,text_color="white",bg_color="transparent", font=("Palatino Linotype", 20), command=self.srchBook)
    self.bsearchBtn.grid(row=0,column=5,padx=20, pady=20)
    
    self.dropdown_frame = ct.CTkFrame(self.existingbookframe_1, fg_color="transparent")
    self.dropdown_frame.grid(row=1, column=0, columnspan=4)


    #############################################
    self.existingbookframe_2 = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    # self.existingbookframe_2.grid(row=2, column=1, pady=20, padx=20, sticky="nsew")

    self.is_running = False
    self.is_existingBook = True
    self.is_newBook = False

    self.booktitleframe = ct.CTkFrame(self.existingbookframe_2, width=600, height=100, fg_color="transparent")
    self.booktitleframe.grid(row=0, column=0, columnspan=6, pady=20, padx=20, sticky="nsew")

    self.booktitle = ct.CTkLabel(self.booktitleframe, text="", fg_color="transparent",justify="center",
                                  text_color="white", font=("arial black", 32))
    self.booktitle.grid(row=0,column=3,padx=20, pady=20,sticky="nsew") 

    self.booktimerlabel1 = ct.CTkLabel(self.existingbookframe_2, text="00:00:00", fg_color="transparent",
                                  text_color="white", font=("Verdana ", 32,"bold"))
    self.booktimerlabel1.grid(row=2,column=3,padx=20, pady=20) 

    image = Image.open("img/sandclock.gif")

    self.sandclockimg1 = ct.CTkImage(light_image=image, size=(100,100))
    

    self.clockimglabel1 = ct.CTkLabel(self.existingbookframe_2, text="", image=self.sandclockimg1 , fg_color="transparent")
    self.clockimglabel1.grid(row=3,column=3,padx=20, pady=20)

    self.bookstartbtn1 = ct.CTkButton(self.existingbookframe_2,text="Start Timer",width=180,height=50,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"), command=self.start)
    self.bookstartbtn1.grid(row=4,column=2,padx=20, pady=20)

    self.bookpausebtn1 = ct.CTkButton(self.existingbookframe_2,text="Pause",width=180,height=50,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"),state="disabled", command=self.pausetimer)
    self.bookpausebtn1.grid(row=4,column=3,padx=20, pady=20)

    self.bookstopbtn1 = ct.CTkButton(self.existingbookframe_2,text="Stop",width=180,height=50,corner_radius=10,text_color="white",bg_color="transparent",font=("arial", 20,"bold"),state="disabled", command=self.stoptimer)
    self.bookstopbtn1.grid(row=4,column=4,padx=20, pady=20)



  
# -----------------------------------------------------    
  def show_book_list(pass):
    pass
# -----------------------------------------------------    
  def show_book_analysis(self):
    pass
# -----------------------------------------------------    
  def addoldbook(self):
    pass
    
# -----------------------------------------------------    

  def backtodashboard1(self):
    self.apptitlelabel.configure(text="Dashboard")
    self.current_book_name=None
    self.gifimgframe.grid_forget()
    self.bookdetailsframe.grid_forget()
    self.bookreadframe.grid_forget()
    self.dashboardframe.grid_configure(row=2, column=0, pady=20, padx=20, sticky="nsew")


  # -----------------------------------------------------    
  
  def backtodashboard2(self):
    try:
      self.backtodashboard1()
      self.booklistframe.grid_forget()
    
    except:
      self.booklistframe.grid_forget()
      self.dashboardframe.grid_configure(row=2, column=0, pady=20, padx=20, sticky="nsew")



# -----------------------------------------------------Main function to run the app-----------------------------------------------------

if __name__ == "__main__":
  app = App()
  app.mainloop()
