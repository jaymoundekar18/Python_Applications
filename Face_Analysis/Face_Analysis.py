# Importing Required Libraries
import cv2
import customtkinter as ct
from PIL import Image, ImageTk
from tkinter import filedialog
from deepface import DeepFace

# App theme
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")


# App Initialization
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Face Analysis App")
        self.geometry("700x700")

        # Initialize variables
        self.video_stream = None
        self.running = False

        self.mainframe = ct.CTkScrollableFrame(self)
        self.mainframe.pack(fill='both', expand=True)


        self.dispImg1 = ct.CTkLabel(self.mainframe, text="")
        self.dispImg1.pack(pady=20)


        self.buttonFrame = ct.CTkFrame(self.mainframe, width=500, height=500, bg_color="transparent")
        self.buttonFrame.pack()

        # Buttons for controlling the app
        self.selectImgButton = ct.CTkButton(self.buttonFrame, text="Select Image", command=self.upimg)
        self.selectImgButton.grid(row=0, column=0, pady=20, padx=20)

        self.liveImgButton = ct.CTkButton(self.buttonFrame, text="Live Camera", command=self.live_cam)
        self.liveImgButton.grid(row=0, column=1, pady=20, padx=20)

        self.endButton = ct.CTkButton(self.buttonFrame, text="Close App", command=self.stop_app)
        self.endButton.grid(row=0, column=2, pady=20, padx=20)

        self.analyzeImage = ct.CTkButton(self.buttonFrame, text="Analyze", command=self.face_analysis)
        self.analyzeImage.grid(row=1, column=1, pady=20, padx=20)

        self.main_image = None
        self.outDispLabel = ct.CTkLabel(self.mainframe, text="")
        self.outDispLabel.pack(pady=20)

    # Uploading Existing Image
    def upimg(self):
        self.stop_live_feed()  

        self.file_path = filedialog.askopenfilename(
            title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if self.file_path:
            img = cv2.imread(self.file_path)
            self.main_image = img
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(img_rgb)
            image = ImageTk.PhotoImage(image)

            self.dispImg1.configure(image=image)
            self.dispImg1.image = image

    # Live Camera Feed
    def live_cam(self):
        self.stop_live_feed()  
        self.video_stream = cv2.VideoCapture(0)
        self.running = True
        self.update_frame()

    def update_frame(self):
        if self.running and self.video_stream is not None:
            ret, frame = self.video_stream.read()

            if ret:
                frame_rgb = cv2.cvtColor(cv2.flip(frame,1), cv2.COLOR_BGR2RGB)
                self.main_image = frame_rgb
                image = Image.fromarray(frame_rgb)
                image = ImageTk.PhotoImage(image)

                self.dispImg1.configure(image=image)
                self.dispImg1.image = image

            self.after(10, self.update_frame)

    def stop_live_feed(self):
        if self.running and self.video_stream is not None:
            self.running = False
            self.video_stream.release()
            self.video_stream = None

    # Face Analysis Using DeepFace
    def face_analysis(self):
        res = DeepFace.analyze(self.main_image)
        feature = ["Emotion", "Face Confidence", "Age", "Gender", "Race"]
        fea_values = []
        for i in res[0]:
                    
                    if isinstance(res[0][i], dict):
                        continue
                    fea_values.append(res[0][i])
        new_text = ""
        for i in range(0,5):
             new_text += f" {feature[i]} : {fea_values[i]} \n"
        
        print(new_text)

        self.outDispLabel.configure(text = new_text)

    def stop_app(self):
        self.stop_live_feed()
        self.destroy()

# Running the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
