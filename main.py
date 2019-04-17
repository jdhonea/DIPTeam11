import cv2
from src.histMatch import histMatch
from src.histEq import histEq
from src.suggest import suggest


if __name__ == "__main__":
    image = []
    hist = []
    # ##########################DEBUGGING ONLY###############################
    image = cv2.imread('LennaGamma.jpg', cv2.IMREAD_GRAYSCALE)
    suggest(image)
    # #######################################################################
    # Draw window
