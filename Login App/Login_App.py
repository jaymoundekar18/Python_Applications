# Importing all the required libraires 

import cv2
from PIL import Image, ImageTk
import customtkinter as ct
from tkinter import messagebox
import sqlite3


# Setting the app appearance and theme
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")


# Database Connection
class dbConnect():
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        print("DB CREATED SUCCESSFULLY")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS login_users (                            
                            full_name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL)''')
        

    def find_User(self,user,password):

        self.cursor.execute("SELECT * FROM login_users WHERE username=? AND password=?", (user, password))
        result = self.cursor.fetchone()
        # print(result)
        return result
        
    def register_User(self,fname, email, user, passwd):

        try:
            self.cursor.execute("INSERT INTO login_users (full_name, email, username, password) VALUES (?,?,?,?)", (fname, email, user, passwd))
            self.conn.commit()
            messagebox.showinfo("Registered",f"Registration Successfull")
        
        except:
            messagebox.showerror("Error", "Please enter details properly")



class App(ct.CTk,dbConnect):
    def __init__(self):
        dbConnect.__init__(self)
        super().__init__() 

        self.title("Login App")
        self.geometry("1200x700")

        # Main frame for the app
        self.main_frame = ct.CTkScrollableFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        # Title Frame
        self.titlelabelframe = ct.CTkFrame(self.main_frame, width=600, height=100, fg_color="transparent")
        self.titlelabelframe.grid(row=0, column=0, columnspan=10,pady=20, padx=20)  

        self.titlelabel = ct.CTkLabel(self.titlelabelframe, text="Login App", fg_color="transparent",
                                      text_color="white", font=("arial black", 32))
        self.titlelabel.pack()  

        
        # Front image frame (on the left side)
        self.frontimgframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
        self.frontimgframe.grid(row=1, column=0, pady=20, padx=20, sticky="nsew")  

        # Front login frame (on the right side)
        self.frontlogframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
        self.frontlogframe.grid(row=1, column=1, pady=20, padx=20, sticky="nsew")

        # Front register frame (on the right side)
        self.frontregframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
        # self.frontregframe.grid(row=1, column=2, pady=20, padx=20, sticky="nsew")



        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)


        # Image configuration on left side
        self.frontimglabel = ct.CTkLabel(self.frontimgframe,text="")
        self.frontimglabel.pack(padx=20, pady=10)

        image1 = cv2.imread("main_img.png")
        imgh, imgw = image1.shape[:2]
        newimgw = int(imgw * 0.7)
        newimgh = int(imgh * 0.7)

        image2 = cv2.resize(image1,(newimgw,newimgh), interpolation=cv2.INTER_AREA)

        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        image2 = Image.fromarray(image2)
        image2 = ImageTk.PhotoImage(image2)
        
        self.frontimglabel.configure(image=image2)
        self.frontimglabel.image = image2

        
        # Login field configuration on right side
               
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
        
        
        img = Image.open("open_eye.png")
        img = img.resize((35, 30))  
        self.eye_open = ImageTk.PhotoImage(img)
        img = Image.open("closed_eye.png")
        img = img.resize((35, 30))  
        self.eye_closed = ImageTk.PhotoImage(img)

        self.eyeButton = ct.CTkButton(self.frontlogframe,image=self.eye_open,corner_radius=20, compound="left",text="",width=40,height=40, command=self.show_password)
        self.eyeButton.grid(row=2,column=4,padx=20, pady=20)
        self.password_visible = False


        self.login_button = ct.CTkButton(self.frontlogframe,text="Login",width=150,height=40,corner_radius=10,text_color="white",bg_color="transparent",fg_color="turquoise",font=("arial", 16), command=self.login)
        self.login_button.grid(row=4,column=3,padx=20, pady=20)

        self.register_button = ct.CTkButton(self.frontlogframe,text="Register",width=150,height=40,corner_radius=10,text_color="white",bg_color="transparent",fg_color="turquoise",font=("arial", 16), command=self.register)
        self.register_button.grid(row=5,column=3,padx=20, pady=20)


        
        # Register field configuration

        self.regnametextlabel = ct.CTkLabel(self.frontregframe,text="Full Name   : ", fg_color="transparent",
                                      text_color="white", font=("Palatino Linotype", 20))
        self.regnametextlabel.grid(row=1,column=2,padx=20, pady=20)

        self.regnameentrylabel = ct.CTkEntry(self.frontregframe,placeholder_text="Enter Your Name",justify="center",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
        self.regnameentrylabel.grid(row=1,column=3,padx=20, pady=20)

        self.regmailtextlabel = ct.CTkLabel(self.frontregframe,text="Email Id   : ", fg_color="transparent",
                                      text_color="white", font=("Palatino Linotype", 20))
        self.regmailtextlabel.grid(row=2,column=2,padx=20, pady=20)

        self.regmailentrylabel = ct.CTkEntry(self.frontregframe,placeholder_text="Enter Your Email ID",justify="center",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
        self.regmailentrylabel.grid(row=2,column=3,padx=20, pady=20)

        self.regusertextlabel = ct.CTkLabel(self.frontregframe,text="User Id   : ", fg_color="transparent",
                                      text_color="white", font=("Palatino Linotype", 20))
        self.regusertextlabel.grid(row=3,column=2,padx=20, pady=20)

        self.reguserentrylabel = ct.CTkEntry(self.frontregframe,placeholder_text="Enter Your User ID",justify="center",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
        self.reguserentrylabel.grid(row=3,column=3,padx=20, pady=20)
        
        self.regpasstextlabel = ct.CTkLabel(self.frontregframe,text="Password    : ", fg_color="transparent",
                                      text_color="white", font=("Palatino Linotype", 20))
        self.regpasstextlabel.grid(row=4,column=2,padx=20, pady=20)

        self.regpassentrylabel = ct.CTkEntry(self.frontregframe,placeholder_text="Enter Your Password",justify="center",show="*",width=350,height=50,bg_color="transparent",fg_color="transparent",font=("arial", 16))
        self.regpassentrylabel.grid(row=4,column=3,padx=20, pady=20)
        
        self.regeyeButton = ct.CTkButton(self.frontregframe,image=self.eye_open,corner_radius=20, compound="left",text="",width=40,height=40, command=self.show_password)
        self.regeyeButton.grid(row=4,column=4,padx=20, pady=20)
        

        self.regSub_button = ct.CTkButton(self.frontregframe,text="Submit",width=150,height=40,corner_radius=10,text_color="white",bg_color="transparent",fg_color="turquoise",font=("arial", 16), command=self.newRegister)
        self.regSub_button.grid(row=6,column=3,padx=20, pady=20)

        self.reglog_button = ct.CTkButton(self.frontregframe,text="Login",width=150,height=40,corner_radius=10,text_color="white",bg_color="transparent",fg_color="turquoise",font=("arial", 16), command=self.backto_login)
        self.reglog_button.grid(row=7,column=3,padx=20, pady=20)


#######################################################################

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



#######################################################################


    def login(self):
        
        if self.frontentrylabel1.get()== '' or self.frontentrylabel2.get() == '':
            messagebox.showwarning("Input Error","Enter UserID and Password")
        
        else:

            
            try:
                result = self.find_User(self.frontentrylabel1.get(),self.frontentrylabel2.get())

                if result is not None:

                    
                    messagebox.showinfo("Login Successful",f"Welcome  {result[0]}")
                    self.changeScreen()


                else:
                    messagebox.showerror("Login Error","Invalid UserId or Password")

            except Exception as e:
                print(e)



#######################################################################

    def register(self):
        print("register clicked")
        self.frontlogframe.grid_forget()
        self.frontregframe.grid_configure(row=1, column=2, pady=20, padx=20, sticky="nsew")


    def newRegister(self):
        if self.regnameentrylabel.get()== '' or self.regmailentrylabel.get() == '' or self.reguserentrylabel.get()== '' or self.regpassentrylabel.get()== '' :
            messagebox.showwarning("Input Error","All fields are required.")
        
        else:

            try:
                self.register_User(self.regnameentrylabel.get(),self.regmailentrylabel.get(),self.reguserentrylabel.get() ,self.regpassentrylabel.get())

                # self.changeScreen()
                self.regnameentrylabel.delete(0, ct.END)
                self.regmailentrylabel.delete(0, ct.END)
                self.reguserentrylabel.delete(0, ct.END)
                self.regpassentrylabel.delete(0, ct.END)
                self.backto_login()
                    

            except Exception as e:
                print(e)



#######################################################################

    def backto_login(self):
        self.frontregframe.grid_forget()
        self.frontlogframe.grid_configure(row=1, column=1, pady=20, padx=20, sticky="nsew")


#######################################################################

    def changeScreen(self):
        self.titlelabel.configure(text="Welcome")
        self.frontimgframe.grid_forget()
        self.frontlogframe.grid_forget()
        self.frontentrylabel1.delete(0, ct.END)
        self.frontentrylabel2.delete(0, ct.END)
        
        self.dashboardframe = ct.CTkFrame(self.main_frame, width=1200, height=700, fg_color="transparent")
        self.dashboardframe.grid(row=1, column=0, pady=20, padx=20, sticky="nsew")
        
        
        self.dashboardlabel = ct.CTkLabel(self.dashboardframe,text="")
        self.dashboardlabel.pack(pady=20, padx=20)

    

        image2 = cv2.imread("dashboard.jpg")
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        image2 = Image.fromarray(image2)
        image2 = ImageTk.PhotoImage(image2)
        
        self.dashboardlabel.configure(image=image2)
        self.dashboardlabel.image = image2



        self.logout_button = ct.CTkButton(self.dashboardframe,text="Logout",width=150,height=40,corner_radius=10,text_color="white",bg_color="transparent",fg_color="turquoise",font=("arial", 16), command=self.logout)
        self.logout_button.pack(padx=20, pady=20)

    


#######################################################################

    def logout(self):
        
        self.dashboardframe.grid_forget()

        self.frontimgframe.grid_configure(row=1, column=0, pady=20, padx=20, sticky="nsew")
        self.frontlogframe.grid_configure(row=1, column=1, pady=20, padx=20, sticky="nsew")




## Main function to run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()

