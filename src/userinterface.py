import numpy as np
from tkinter import Image, filedialog, Label, Button, Tk, Menu, Frame
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import matplotlib.pyplot as plt
import cv2

class GUIclass:
    def __init__(self, window):
        #window is a tk object
        self.window=window
        #title
        window.title("COSC 4393 Final Project")

        #menubar
        menu=Menu(window)
        window.config(menu=menu)

        filemenu=Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)

        filemenu.add_command(label="Open...", command=self.open_file)
        #filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="Exit", command=window.quit)

        #radio buttons
        menuitem=Menu(window)
        trans=Menu(window)
        menu.add_cascade(label="Transformations", menu=trans)
        trans.add_radiobutton(label="Negative", command=self.choose_op())
        trans.add_radiobutton(label="Option 2", command=self.choose_op())

        # self.label=Label(window, text="first gui")
        # self.label.pack()
        #
        # self.button=Button(window, text="Transformation", command=self.Transformation)
        # self.button.pack()
        #
        # self.button=Button(window, text="Choose Image", command=self.open_file)
        # self.button.pack()
        #self.button.place(height=100, width=100)


    def choose_op(self):
        print("hello")


    def open_file(self):
        path=filedialog.askopenfilename(filetypes=[("Image File", 'jpg', '.png')])
        im=Image.open(path)
        tkimage=ImageTk.PhotoImage(im)
        label=Label(self.window, image=tkimage)
        label.image=tkimage
        label.pack(side=LEFT, padx=50)


# win=Tk()
# # height x width
# win.geometry("1920x1080")
# # win.resizable(0,0)
# GUI=GUIclass(win)
# win.mainloop()

