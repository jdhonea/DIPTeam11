import cv2
from src.histogram import Hist
from src.histEq import histEq

if __name__ == "__main__":
    image = []
    hist = []
    # ##########################DEBUGGING ONLY###############################
    image = cv2.imread('bean.png', cv2.IMREAD_GRAYSCALE)
    hist = Hist(image)
    # #######################################################################
    # Draw window   