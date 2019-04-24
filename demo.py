import cv2
import numpy as np
from src.histEq import histEq
from src.histMatch import histMatch
from src.imgNeg import imgNegative
from src.miscFuncts import displayImage
from src.powerLawGamma import powerLaw
from src.Contrast_Stretch import contrast_str
from src.suggest import suggest
from src.histogram import Hist

if __name__ == "__main__":
    print("Team 11 Demo")
    command = input()
    image = cv2.imread("Lenna0.jpg", cv2.IMREAD_GRAYSCALE)
    target = cv2.imread("bean.png", cv2.IMREAD_GRAYSCALE)
    while command != "exit":
        #print(command)
        if command == "image":
            command = input("Image name: ")
            image = cv2.imread(command, cv2.IMREAD_GRAYSCALE)
            displayImage("image", image)
        elif command == "target":
            command = input("Target Image: ")
            target = cv2.imread(command, cv2.IMREAD_GRAYSCALE)
            displayImage("target", target)
        elif command == "equalization":
            (newimage, histogram) = histEq(image)
            displayimage = np.hstack((image, newimage))
            displayImage("Equalization", displayimage)
        elif command == "matching":
            (newimage, histogram) = histMatch(image, target)
            displayimage = np.hstack((image,newimage))
            displayImage("Matching", displayimage)
        elif command == "negative":
            newimage = imgNegative(image)
            displayimage = np.hstack((image,newimage))
            displayImage("Negative", displayimage)
        elif command == "stretch":
            newimage = contrast_str(image)
            displayimage = np.hstack((image, newimage))
            displayImage("Stretch", displayimage)
        elif command == "power":
            gamma = input("Gamma value: ")
            newimage = powerLaw(image, float(gamma))
            displayimage = np.hstack((image, newimage))
            displayImage("Power Law", displayimage)
        elif command == "shaping":
            hist = Hist(image)
            shape = input("Target Histograms: \n1. Bell Shaped\n2. Bimodal\n3. Right Skewed\n4. J Shaped\n5. U Shaped\n")
            newimage = hist.HistShap(hist.app_spec_hist()[int(shape) - 1])
            displayimage = np.hstack((image, newimage))
            displayImage("Shaping", displayimage)
        elif command == "suggest":
            suggestion = suggest(image)
            print(suggestion)

        command = input()