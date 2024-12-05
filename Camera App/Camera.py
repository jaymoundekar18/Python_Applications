# Importing Required Libraries
import cv2
import customtkinter as ct
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

# App theme
ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

# App Initialization
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Camera")
        
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # Set the window to full screen resolution
        self.geometry(f"{self.screen_width}x{self.screen_height}")

        # Initialize video capture
        self.video_stream = cv2.VideoCapture(0)
        if not self.video_stream.isOpened():
            messagebox.showerror("Error", "Failed to open the camera")
            self.destroy()
            return

        # Main frame
        self.mainframe = ct.CTkScrollableFrame(self)
        self.mainframe.pack(fill='both', expand=True)

        # Camera frame to display video feed
        self.camera_frame = ct.CTkLabel(self.mainframe, text="")
        self.camera_frame.pack(pady=20)

        self.update_frame()

        # Buttons frame
        self.buttonFrame = ct.CTkFrame(self.mainframe, width=500, height=500, bg_color="transparent")
        self.buttonFrame.pack()

        self.captureImgButton = ct.CTkButton(self.buttonFrame, text="Capture Image", command=self.saveImage)
        self.captureImgButton.grid(row=0, column=0, pady=20, padx=20)

        self.endButton = ct.CTkButton(self.buttonFrame, text="Close App", command=self.stop_app)
        self.endButton.grid(row=0, column=1, pady=20, padx=20)

        self.main_image = None

    def update_frame(self):
        # Read video stream frame
        ret, frame = self.video_stream.read()

        if ret:
            frame = cv2.resize(frame, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)
            
            frame_rgb = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

            self.main_image = frame_rgb  # Save the latest frame for capturing
            image = Image.fromarray(frame_rgb)
            image = ImageTk.PhotoImage(image)

            self.camera_frame.configure(image=image)
            self.camera_frame.image = image

        self.after(10, self.update_frame)

    def saveImage(self):
        if self.main_image is None:
            messagebox.showerror("Error", "No image to save")
            return


        save_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG Files", "*.png"),("JPEG Files", "*.jpg"),("All Files", "*.*")])
        
        if save_path:
            
            try:
                cv2.imwrite(save_path, cv2.cvtColor(self.main_image, cv2.COLOR_RGB2BGR))
                messagebox.showinfo("Image Captured", f"Image saved successfully at {save_path}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save the image: {e}")

    def stop_app(self):
        self.video_stream.release()
        self.destroy()

# Running the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
