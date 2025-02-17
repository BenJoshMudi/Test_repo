from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter


class Face_Recognition_System:
    def __init__(self, root):
        self.root=root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #First Image
        img1 = Image.open(r"C:/Users/mudia/Downloads/SChool building img.jpeg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width= 500, height=130)

        #Second Image
        img2 = Image.open(r"C:/Users/mudia/Downloads/facial_images.jpeg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width= 550, height=130)

        #Third Image
        img3 = Image.open(r"C:/Users/mudia/Downloads/gomycode.jpeg")
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width= 550, height=130)

        #Bg image
        img4 = Image.open(r"C:/Users/mudia\Downloads/testbg.jpg")
        
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
        img4 = img4.filter(ImageFilter.SHARPEN)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width= 1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0, width=1530, height=45)

        #student button
        img5 = Image.open(r"C:/Users/mudia/Downloads/student_image.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor = "hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1= Button(bg_img, text="Student Details", cursor="hand2", font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        #Detector face button
        img6 = Image.open(r"C:/Users/mudia/Downloads/face_detect.png")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor = "hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1= Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        #Attendance face button
        img7 = Image.open(r"C:/Users/mudia/Downloads/attendimag.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor = "hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1= Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

         #Help Desk Button
        img8 = Image.open(r"C:/Users/mudia/Downloads/help.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor = "hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1= Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        
         #Train Face Button
        img9 = Image.open(r"C:/Users/mudia/Downloads/trainf.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor = "hand2")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1= Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)


        # Photos face button
        img11 = Image.open(r"C:/Users/mudia/Downloads/photo.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor = "hand2")
        b1.place(x=500, y=380, width=220, height=220)

        b1_1= Button(bg_img, text="Photo", cursor="hand2", font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

         # Developer button
        img10 = Image.open(r"C:/Users/mudia/Downloads/developer.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor = "hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1= Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)
        
         # Exit button
        img12 = Image.open(r"C:/Users/mudia/Downloads/Exit.png")
        img12 = img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_img, image=self.photoimg12, cursor = "hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1= Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)


        






if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()