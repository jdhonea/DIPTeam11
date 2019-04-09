import cv2
from src.histMatch import histMatch
from src.histEq import histEq
from src.suggest import suggest

if __name__ == "__main__":
    image = []
    hist = []
    # ##########################DEBUGGING ONLY###############################
    image = cv2.imread('Lenna0.jpg', cv2.IMREAD_GRAYSCALE)
    # #######################################################################
    # Draw window   