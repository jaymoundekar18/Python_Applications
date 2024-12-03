# Importing Required Libraries

import cv2
from facenet_pytorch import MTCNN
import customtkinter as ct
from PIL import Image, ImageTk
from tkinter import filedialog

# App theme
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

# Creating face detector
detector = MTCNN()

# App Initialization
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Face Extraction App")
        self.geometry("700x700")
        
        self.mainframe = ct.CTkScrollableFrame(self)
        self.mainframe.pack(fill='both', expand=True)

        self.frame_label = ct.CTkLabel(self.mainframe, text="")
        self.frame_label.pack(pady=20)

        self.dispImg1 = ct.CTkLabel(self.mainframe, text="")
        self.dispImg1.pack(pady=20)
        
        self.extractFrame = ct.CTkFrame(self.mainframe, width=500, height=500, bg_color="transparent")

        self.buttonFrame = ct.CTkFrame(self.mainframe, width=500, height=500, bg_color="transparent")
        self.buttonFrame.pack()

       
        self.startButton = ct.CTkButton(self.buttonFrame, text="Select Image", command=self.upimg)
        self.startButton.grid(row=1, column=0, pady=20, padx=20)

        self.extractButton = ct.CTkButton(self.buttonFrame, text="Extract Face", command=self.extract)
        self.extractButton.grid(row=1, column=1, pady=20, padx=20)

        self.endButton = ct.CTkButton(self.buttonFrame, text="Close App", command=self.stop_app)
        self.endButton.grid(row=1, column=2, pady=20, padx=20)

    def upimg(self):
        self.extractFrame.pack_forget()
        self.file_path = filedialog.askopenfilename(title="Select an Image", 
                                                    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if self.file_path:
            print(f"File Path: {self.file_path}")

            img = cv2.imread(self.file_path)
            print(img.shape)

            image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)

            self.dispImg1.configure(image=image)
            self.dispImg1.image = image

    def extract(self):
        if not hasattr(self, "file_path") or not self.file_path:
            print("No image selected!")
            return
        
        for widget in self.extractFrame.winfo_children():
            widget.destroy()
        self.extractFrame.pack(pady=20)

        img = cv2.imread(self.file_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        faces, _ = detector.detect(img_rgb)

        if faces is not None:
            for i, face in enumerate(faces):
                x1, y1, x2, y2 = map(int, face)

                cropped_face = img_rgb[y1:y2, x1:x2]
                cropped_face = Image.fromarray(cropped_face)
                cropped_face.thumbnail((100, 100))  

                face_image = ImageTk.PhotoImage(cropped_face)

                row = i // 5  
                column = i % 5

                face_label = ct.CTkLabel(self.extractFrame, text='', image=face_image)
                face_label.image = face_image 
                face_label.grid(row=row, column=column, padx=10, pady=10)

            print(f"Extracted {len(faces)} faces.")

        else:
            print("No faces detected.")
            empty_label = ct.CTkLabel(self.extractFrame, text="No Faces Detected")
            empty_label.grid(row=0, column=0, padx=10, pady=10)

    def stop_app(self):
        self.destroy()

# Running the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
