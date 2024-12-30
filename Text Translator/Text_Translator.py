# Import Required Libraries

import customtkinter as ct
from tkinter import messagebox
from deep_translator import GoogleTranslator


# Setting the app appearance and theme
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

class TranslatorApp(ct.CTk):

  def __init__(self):
    pass


if __name__=="__main__":
  TranslatorApp().mainloop() 
