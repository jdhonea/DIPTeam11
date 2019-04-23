#import
import numpy as np
#from
from userinterface import GUIclass
from tkinter import *

if __name__=="__main__":
    win = Tk()
    # height x width
    win.geometry("1920x1080")
    # win.resizable(0,0)
    GUI = GUIclass(win)
    win.mainloop()