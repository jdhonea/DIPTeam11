import cv2
from src.histogram import Hist
from src.histEq import histEq

if __name__ == "__main__":
    image = []
    hist = []
    # ##########################DEBUGGING ONLY###############################
    image = cv2.imread('Lenna0.jpg', cv2.IMREAD_GRAYSCALE)
    hist = Hist(image)
    # #######################################################################
    # Draw window   