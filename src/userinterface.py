import numpy as np
from tkinter import Image, filedialog, Label, Button, Tk, Menu, Frame, simpledialog, messagebox
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import cv2

from src.histMatch import histMatch
from src.histEq import histEq
from src.suggest import suggest
from src.miscFuncts import displayImage
from src.powerLawGamma import powerLaw
from src.Contrast_Stretch import contrast_str
from src.imgNeg import imgNegative
from src.log_transform import LogTransform

class GUIclass:
    def __init__(self, window):
        #window is a tk object
        self.window=window
        #to choose operation
        self.operation=""
        #to apply operation
        self.image=tk.Image
        self.image_matrix=np.zeros((5,5))
        #to clear image
        self.image_label=tk.Label
        #title
        window.title("COSC 4393 Final Project")

        #menubar
        menu=Menu(window)
        window.config(menu=menu)

        filemenu=Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)

        filemenu.add_command(label="Open...", command=self.open_file)
        filemenu.add_command(label="Save New Image As...", command=self.save_file)
        filemenu.add_command(label="Exit", command=window.quit)

        #radio buttons
        menuitem=Menu(window)
        trans=Menu(window)
        menu.add_cascade(label="Transformations", menu=trans)
        trans.add_radiobutton(label="Contrast Stretch", command=self.set_contrast_stretch)
        trans.add_radiobutton(label="Histogram Equalization", command=self.set_histogram_equalization)
        #equalized?
        trans.add_radiobutton(label="Image Negative", command=self.set_negative)
        trans.add_radiobutton(label="Log Transform", command=self.set_log_transform)
        trans.add_radiobutton(label="Power Law Gamma", command=self.set_pl_gamma)


        #translation button
        self.button=Button(window, text="Apply", command=self.transformation)
        self.button.pack(side=BOTTOM)

        # clear button
        self.button = Button(window, text="Clear", command=self.clear_image)
        self.button.pack(side=BOTTOM)

        #show suggestion
        self.button = Button(window, text="Suggest Transform", command=self.show_suggest)
        self.button.pack(side=BOTTOM)

        #filler labels for images


        # self.button=Button(window, text="Transformation", command=self.Transformation)
        # self.button.pack()
        #
        # self.button=Button(window, text="Choose Image", command=self.open_file)
        # self.button.pack()
        #self.button.place(height=100, width=100)

    def set_contrast_stretch(self):
        self.operation="contraststr"
        print("Contrast Stretch chosen")

    def set_histogram_equalization(self):
        self.operation="histeq"
        print("Histogram Equalization chosen")

    def set_negative(self):
        self.operation="imgneg"
        print("Image Negative chosen")

    def set_log_transform(self):
        self.operation="logtran"
        print("Log Transform chosen")

    def set_pl_gamma(self):
        self.operation="plg"
        print("Power Law Gamma chosen")

    def clear_image(self):
        self.image_label.destroy()

    def show_suggest(self):
        arr=self.image_matrix
        suggestion=suggest(arr)
        messagebox.showinfo("Suggestion", suggestion)
        print(suggestion)

    def transformation(self):
        #self.clear_image()
        #self.image_label.destroy()
        old_label=self.image_label
        #if old_label.winfo_exists():
        #    print("WINDOW EXISTS")

        tkimage = self.image
        img_matrix=self.image_matrix

        if self.operation=="contraststr":
            print("Constrast stretch applied")
            img_matrix=contrast_str(img_matrix)
            img=Image.fromarray(img_matrix)
            tkimage=ImageTk.PhotoImage(img)

        elif self.operation=="histeq":
            print("Histogram Equalization applied")
            img_matrix, histogram=histEq(img_matrix)
            img=Image.fromarray(img_matrix)
            tkimage=ImageTk.PhotoImage(img)

        elif self.operation=="imgneg":
            print("Image Negative applied")
            img_matrix=imgNegative(img_matrix)
            img=Image.fromarray(img_matrix)
            tkimage=ImageTk.PhotoImage(img)

        elif self.operation=="logtran":
            print("Log Transform applied")
            val=simpledialog.askfloat("C value:", "What is the c value?")
            log=LogTransform()
            img_matrix=LogTransform.log_transform(log, img_matrix, val)
            img=Image.fromarray(img_matrix)
            tkimage=ImageTk.PhotoImage(img)

        elif self.operation=="plg":
            print("Power Gamma Law applied")
            val = simpledialog.askfloat("Gamma:", "What is the gamma value?")
            img_matrix=powerLaw(img_matrix, 2)
            img=Image.fromarray(img_matrix)
            tkimage=ImageTk.PhotoImage(img)

        else:
            print("Error, incorrect selection.")

        label = Label(self.window, image=tkimage)
        label.image = tkimage
        label.pack(side=RIGHT, padx=50, expand=TRUE)
        self.image_label = label

    def open_file(self):
        #open image
        path=filedialog.askopenfilename(filetypes=[("Image File", "*")])
        im=Image.open(path)
        tkimage=ImageTk.PhotoImage(im)
        img=Image.open(path).convert("L")
        arr=np.array(img)

        #show image
        self.image = tkimage
        self.image_matrix=arr
        label=Label(self.window, image=tkimage)
        #label.configure(image=tkimage)
        label.image=tkimage
        label.pack(side=LEFT, ipadx=125)

    def save_file(self):
        path=filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

    def get_image(self):
        print("get")

    def set_image(self):
        print("set")


win=Tk()
# height x width
win.geometry("1600x700")
# win.resizable(0,0)
GUI=GUIclass(win)
win.mainloop()