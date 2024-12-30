# Import Required Libraries

import customtkinter as ct
from tkinter import messagebox
from deep_translator import GoogleTranslator


# Setting the app appearance and theme
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

# App Initialization
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

    # Splitting main frame into two parts
    self.sourcetextframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    self.sourcetextframe.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")  

    self.targettextframe = ct.CTkFrame(self.main_frame, width=1200 // 2, height=700, fg_color="transparent")
    self.targettextframe.grid(row=2, column=1, pady=20, padx=20, sticky="nsew")

    
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_frame.grid_columnconfigure(1, weight=1)
    self.main_frame.grid_rowconfigure(1, weight=1)

    self.languages_code = {'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Assamese': 'as', 'Aymara': 'ay', 'Azerbaijani': 'az', 'Bambara': 'bm',
 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bhojpuri': 'bho', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese (simplified)': 'zh-CN',
 'Chinese (traditional)': 'zh-TW', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dhivehi': 'dv', 'Dogri': 'doi', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 
 'Estonian': 'et', 'Ewe': 'ee', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Guarani': 'gn', 
 'Gujarati': 'gu', 'Haitian creole': 'ht', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'iw', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Ilocano': 'ilo',
 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Kinyarwanda': 'rw', 'Konkani': 'gom', 'Korean': 'ko', 
 'Krio': 'kri', 'Kurdish (kurmanji)': 'ku', 'Kurdish (sorani)': 'ckb', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lingala': 'ln', 'Lithuanian': 'lt', 'Luganda': 'lg', 
 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Maithili': 'mai', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Meiteilon (manipuri)': 'mni-Mtei',
 'Mizo': 'lus', 'Mongolian': 'mn', 'Myanmar': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia (oriya)': 'or', 'Oromo': 'om', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 
 'Punjabi': 'pa', 'Quechua': 'qu', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Sanskrit': 'sa', 'Scots gaelic': 'gd', 'Sepedi': 'nso', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 
 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Tatar': 'tt', 
 'Telugu': 'te', 'Thai': 'th', 'Tigrinya': 'ti', 'Tsonga': 'ts', 'Turkish': 'tr', 'Turkmen': 'tk', 'Twi': 'ak', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 
 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}

    languages = list(self.languages_code.keys())
    languages.insert(0,"--Select--")

    self.srclanglabel = ct.CTkLabel(self.sourcetextframe,text="Select Language : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.srclanglabel.grid(row=0,column=1,padx=20, pady=20)

    self.srclangoption = ct.CTkOptionMenu(self.sourcetextframe, values=languages, width=200, height=40)
    self.srclangoption.grid(row=0, column= 2, padx=20, pady=20)
    
    # User Text Input Field
    self.textentrylabel1 = ct.CTkTextbox(self.sourcetextframe,width=550,height=550,bg_color="#3d3d3d",fg_color="transparent",font=("Palatino Linotype", 20))
    self.textentrylabel1.grid(row=2,column=0, columnspan=4,padx=20, pady=20)
    self.textentrylabel1.insert("0.0", "Enter Your text")
    self.textentrylabel1.bind("<KeyRelease>", self.convert)
    
    

    self.tarlanglabel = ct.CTkLabel(self.targettextframe,text="Select Language : ", fg_color="transparent",
                                  text_color="white", font=("Palatino Linotype", 20))
    self.tarlanglabel.grid(row=0,column=1,padx=20, pady=20)

    self.tarlangoption = ct.CTkOptionMenu(self.targettextframe, values=languages, width=200, height=40)
    self.tarlangoption.grid(row=0, column= 2, padx=20, pady=20)
    
    # Translated Text Output Field
    self.transentrylabel1 = ct.CTkTextbox(self.targettextframe, width=550,height=550, bg_color="#3d3d3d", fg_color="transparent", font=("Palatino Linotype", 20))
    self.transentrylabel1.grid(row=2, column=0, columnspan=4, padx=20, pady=20)

  # Convert / Translate Text Function
  def convert(self, event):
    if self.srclangoption.get() != "--Select--" and self.tarlangoption.get() != "--Select--":
                  
        transtext = self.textentrylabel1.get("0.0", "end-1c")
        if transtext:
            txt = GoogleTranslator(source=self.languages_code[self.srclangoption.get()], target=self.languages_code[self.tarlangoption.get()]).translate(transtext)
            
            self.transentrylabel1.delete("0.0","end")
            self.transentrylabel1.insert("0.0", txt)

        else:
            self.transentrylabel1.delete("0.0","end")
    
    else:
        messagebox.showwarning("Warning", "Select Languages !")

# Running the app
if __name__=="__main__":
  TranslatorApp().mainloop() 
