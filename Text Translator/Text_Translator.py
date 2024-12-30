# Import Required Libraries

import customtkinter as ct
from tkinter import messagebox
from deep_translator import GoogleTranslator


# Setting the app appearance and theme
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

class TranslatorApp(ct.CTk):

  def __init__(self):
    super().__init__()
    app_width = self.winfo_screenwidth()
    app_height = self.winfo_screenheight()\

    self.geometry(f"{app_width}x{app_height}")
    self.title("Translator")

    # Main frame for the app
    self.main_frame = ct.CTkScrollableFrame(self)
    self.main_frame.pack(fill='both', expand=True)

    # Title Frame
    self.titlelabelframe = ct.CTkFrame(self.main_frame, width=600, height=100, fg_color="transparent")
    self.titlelabelframe.grid(row=0, column=0, columnspan=10,pady=20, padx=20)  

    self.apptitlelabel = ct.CTkLabel(self.titlelabelframe, text="Text Translator App", fg_color="transparent",
                                  text_color="white", font=("arial black", 38))
    self.apptitlelabel.pack()  

    
    self.sourcetextframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    self.sourcetextframe.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")  

    self.targettextframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    self.targettextframe.grid(row=2, column=1, pady=20, padx=20, sticky="nsew")

    
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_frame.grid_columnconfigure(1, weight=1)
    self.main_frame.grid_rowconfigure(1, weight=1)

     


if __name__=="__main__":
  TranslatorApp().mainloop() 
