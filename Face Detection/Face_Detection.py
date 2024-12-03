# Importing Required Librarires

import cv2
from facenet_pytorch import MTCNN
import customtkinter as ct
from PIL import Image, ImageTk

# App theme 
ct.set_appearance_mode("dark")        
ct.set_default_color_theme("blue") 

# Creating face detector
detector = MTCNN()

# App Initialization
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Face Detection App")
        self.geometry("700x700")

        # Initialize face detection flag
        self.facedetection = False

        # Initialize video capture
        self.video_stream = cv2.VideoCapture(0)

        # Creating labels to display frames and results
        self.frame_label = ct.CTkLabel(self, text="")
        self.frame_label.pack(pady=20)

        self.displabel = ct.CTkLabel(self, text="")
        self.displabel.pack(pady=20)

        # Start frame update
        self.update_frame()

        # Create frame for buttons
        self.buttonFrame = ct.CTkFrame(self, width=500, height=500, bg_color="transparent")
        self.buttonFrame.pack()

        # Buttons for controlling detection
        self.startButton = ct.CTkButton(self.buttonFrame, text="Start Detection", width=120, height=50, command=self.start_detection)
        self.startButton.grid(row=1, column=0, pady=20, padx=20)

        self.stopButton = ct.CTkButton(self.buttonFrame, text="Stop Detection", width=120, height=50, command=self.stop_detection)
        self.stopButton.grid(row=1, column=1, pady=20, padx=20)

        self.endButton = ct.CTkButton(self.buttonFrame, text="Close App", width=120, height=50, command=self.stop_app)
        self.endButton.grid(row=1, column=2, pady=20, padx=20)

    def update_frame(self):
        ret, frame = self.video_stream.read()

        if ret:
            if self.facedetection:
                frame_pil = Image.fromarray(frame)
                faces, _ = detector.detect(frame_pil)

                if faces is not None:
                    self.displabel.configure(text="Face Detected")
                    for face in faces:
                        x, y, w, h = map(int, face)
                        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
                else:
                    self.displabel.configure(text="No Face Detected")
            
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image = ImageTk.PhotoImage(image)

            self.frame_label.configure(image=image)
            self.frame_label.image = image  

        self.after(1, self.update_frame)

    def start_detection(self):
        self.facedetection = True
        print("Detection started")

    def stop_detection(self):
        self.facedetection = False
        print("Detection stopped")

    def stop_app(self):
        self.video_stream.release()  
        self.destroy()

# Running the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
