import cv2
from src.histogram import Hist
from src.histEq import histEqual as eq

# DEBUGGING ONLY
def display_image(window_name, image):
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


if __name__ == "__main__":
    image = []
    hist = []
    # ##########################DEBUGGING ONLY###############################
    image = cv2.imread('Lenna0.jpg', cv2.IMREAD_GRAYSCALE)
    hist = Hist(image)
    # #######################################################################
    # Draw window   