import numpy as np
from tkinter import Image, filedialog, Label, Button, Tk, Menu, Frame
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import cv2

from src.histMatch import histMatch
from src.histEq import histEq
from src.suggest import suggest
from src.miscFuncts import displayImage
from src.powerLawGamma import powerLaw
from src.imgNeg import imgNegative

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
        trans.add_radiobutton(label="Negative", command=self.set_negative)
        #trans.add_radiobutton(label="Option 2", command=self.choose_op())

        #translation button
        self.button=Button(window, text="Apply", command=self.transformation)
        self.button.pack(side=BOTTOM)

        # clear button
        self.button = Button(window, text="Clear", command=self.clear_image)
        self.button.pack(side=BOTTOM)


        # self.button=Button(window, text="Transformation", command=self.Transformation)
        # self.button.pack()
        #
        # self.button=Button(window, text="Choose Image", command=self.open_file)
        # self.button.pack()
        #self.button.place(height=100, width=100)

    def set_negative(self):
        self.operation="Negative"
        print("Negative chosen")

    def clear_image(self):
        self.image_label.destroy()

    def transformation(self):
        #self.clear_image()
        #self.image_label.destroy()
        tkimage = self.image
        img_matrix=self.image_matrix

        if self.operation=="Negative":
            print("Negative applied")
            #print(img_matrix.shape)
            img_matrix=imgNegative(img_matrix)
            img=Image.fromarray(img_matrix)
            tkimage=ImageTk.PhotoImage(img)

        label = Label(self.window, image=tkimage)
        label.image = tkimage
        label.pack(side=RIGHT, padx=50, expand=TRUE)
        self.image_label = label

    def open_file(self):
        path=filedialog.askopenfilename(filetypes=[("Image File", 'jpg', '.png')])
        im=Image.open(path)
        tkimage=ImageTk.PhotoImage(im)
        img=Image.open(path)
        arr=np.array(img)
        self.image = tkimage
        self.image_matrix=arr
        label=Label(self.window, image=tkimage)
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

