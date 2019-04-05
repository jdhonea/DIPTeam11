import cv2
from src.histogram import Hist

if __name__ == "__main__":
    image = []
    hist = []
    image = cv2.imread('Lenna0.jpg', cv2.IMREAD_GRAYSCALE)
    Hist(image)
    #Draw window   