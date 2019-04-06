import cv2
from src.histMatch import histMatch

if __name__ == "__main__":
    image = []
    hist = []
    # ##########################DEBUGGING ONLY###############################
    image = cv2.imread('bean.png', cv2.IMREAD_GRAYSCALE)
    target = cv2.imread('Lenna0.jpg', cv2.IMREAD_GRAYSCALE)
    histMatch(image, target)
    # #######################################################################
    # Draw window   