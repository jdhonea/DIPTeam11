import cv2
from src.histMatch import histMatch
from src.histEq import histEq
from src.suggest import suggest
from src.userinterface import GUIclass
from tkinter import *

if __name__ == "__main__":
    win = Tk()
    # height x width
    win.geometry("1920x1080")
    # win.resizable(0,0)
    GUI = GUIclass(win)
    win.mainloop()