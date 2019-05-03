import numpy as np
from tkinter import Image, filedialog, Label, Button, Tk, Menu, Frame, simpledialog, messagebox
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import cv2

from src.histMatch import histMatch
from src.histEq import histEq
from src.histogram import Hist
from src.suggest import suggest
from src.powerLawGamma import powerLaw
from src.Contrast_Stretch import contrast_str
from src.imgNeg import imgNegative
from src.log_transform import LogTransform

class GUIclass:
    def __init__(self, window):
        #set references
        self.window=window
        self.operation=""
        self.image=""
        self.image_matrix=np.zeros((5,5))
        self.image_label=tk.Label
        self.newimage=""
        self.originallabel=""
        #title
        window.title("COSC 4393 Final Project")

        #menubar
        menu=Menu(window)
        window.config(menu=menu)
        filemenu=Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open...", command=self.open_file)
        filemenu.add_command(label="Save New Image As...", command=self.save_file)
        filemenu.add_command(label="Clear All Images", command=self.clear_all)
        filemenu.add_command(label="Exit", command=window.quit)

        #radio buttons
        trans=Menu(window)
        menu.add_cascade(label="Transformations", menu=trans)
        trans.add_radiobutton(label="Contrast Stretch", command=self.set_contrast_stretch)
        trans.add_radiobutton(label="Histogram Equalization", command=self.set_histogram_equalization)
        trans.add_radiobutton(label="Histogram Matching", command=self.set_histogram_matching)
        trans.add_radiobutton(label="Histogram Shaping", command=self.set_histogram_shaping)
        trans.add_radiobutton(label="Image Negative", command=self.set_negative)
        trans.add_radiobutton(label="Log Transform", command=self.set_log_transform)
        trans.add_radiobutton(label="Power Law Gamma", command=self.set_pl_gamma)

        #apply button
        self.button=Button(window, text="Apply", command=self.transformation, height=2, width=25)
        self.button.pack(side=BOTTOM)

        #show suggestion
        self.button = Button(window, text="Suggest Transform", command=self.show_suggest, height=2, width=20)
        self.button.pack(side=TOP)

    def set_contrast_stretch(self):
        self.operation="contraststr"
        print("Contrast Stretch chosen")

    def set_histogram_equalization(self):
        self.operation="histeq"
        print("Histogram Equalization chosen")

    def set_histogram_matching(self):
        self.operation="histmat"
        print("Histogram Matching chosen")

    def set_histogram_shaping(self):
        self.operation="histshap"
        print("Histogram Shaping chosen")

    def set_negative(self):
        self.operation="imgneg"
        print("Image Negative chosen")

    def set_log_transform(self):
        self.operation="logtran"
        print("Log Transform chosen")

    def set_pl_gamma(self):
        self.operation="plg"
        print("Power Law Gamma chosen")

    def show_suggest(self):
        if not self.image:
            messagebox.showerror("Error", "No image chosen!")
            return None

        arr=self.image_matrix
        suggestion=suggest(arr)
        messagebox.showinfo("Suggestion", suggestion)
        print(suggestion)

    def transformation(self):
        if self.newimage:
            self.image_label.destroy()
            self.image_label=""

        tkimage = self.image
        img_matrix=self.image_matrix

        #check if image is present
        if not tkimage:
            print("No image selected!")
            messagebox.showerror("Error", "No image chosen!")
            return None

        #check if operation is chosen
        if not self.operation:
            messagebox.showwarning("Warning", "No transformation chosen!")
            return None

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

        elif self.operation=="histmat":
            print("Histogram Matching applied")
            # open image
            path = filedialog.askopenfilename(filetypes=[("Image File", "*")])
            img = Image.open(path).convert("L")
            arr = np.array(img)

            img_matrix, histogram=histMatch(img_matrix, arr)
            img=Image.fromarray(img_matrix)
            tkimage=ImageTk.PhotoImage(img)

        elif self.operation=="histshap":
            print("Histogram Shaping applied")
            val=simpledialog.askstring("Select a value:", "Target Histograms: \n1. Bell Shaped\n2. Bimodal\n3. Right Skewed\n4. J Shaped\n5. U Shaped\nExample input: 3\n")
            hist=Hist(img_matrix)
            img_matrix=hist.HistShap(hist.app_spec_hist()[int(val)-1])
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
            img_matrix=powerLaw(img_matrix, val)
            img=Image.fromarray(img_matrix)
            tkimage=ImageTk.PhotoImage(img)

        else:
            print("Error, incorrect selection.")

        label = Label(self.window, image=tkimage)
        label.image = tkimage
        label.pack(side=RIGHT, padx=50, expand=TRUE)
        self.image_label = label
        self.newimage=img

    def open_file(self):
        #open image
        path=filedialog.askopenfilename(filetypes=[("All files", "*"), ("JPEG files", "*.jpg"), ("PNG files", "*.png")])

        if self.image:
            self.originallabel.forget()

        if path:
            im=Image.open(path)
            tkimage=ImageTk.PhotoImage(im)
            img=Image.open(path).convert("L")
            arr=np.array(img)

            #show image
            self.image = tkimage
            self.image_matrix=arr
            label=Label(self.window, image=tkimage)
            self.originallabel=label
            label.image=tkimage
            label.pack(side=LEFT, ipadx=125)

    def save_file(self):
        if not self.newimage:
            messagebox.showwarning("Warning", "No transformed image!")
            return None

        path=filedialog.asksaveasfilename(initialdir = "/", title = "Select file", defaultextension=".jpg" ,filetypes = [("JPEG files", "*.jpg"), ("PNG files", "*.png")])
        if path:
            self.newimage.save(path)

    def clear_all(self):
        if self.newimage:
            self.image_label.destroy()
            self.newimage=""

        if self.image:
            self.originallabel.destroy()
            self.image=""