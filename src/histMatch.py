from .histogram import Hist
import numpy as np
from .miscFuncts import displayImage
import matplotlib.pyplot as plt


def histMatch(image, target):
    # Receives an image and a target image
    # Returns image and histogram
    hist = []
    imageHist = Hist(image)
    targetHist = Hist(target)
    imgCDF = imageHist.cdf
    targetCDF = targetHist.cdf
    imgCDF = [int(x * 255) for x in imgCDF]
    targetCDF = [int(x * 255) for x in targetCDF]
    displayImage("Original", image)
    plt.plot(imageHist.hist)
    plt.plot(targetHist.hist)
    image = calculateImage(image, imgCDF, targetCDF)
    displayImage("Matched", image)
    newHist = Hist(image)
    plt.plot(newHist.hist)
    plt.show()
    return (image, hist)


def calculateImage(image, src, target):
    newImage = np.zeros(image.shape, np.uint8())
    for row in range(0, newImage.shape[0]):
        for col in range(0, newImage.shape[1]):
            intermedValue = src[image[row][col]]  # Grabs the CDF value from the src image
            for value in target:
                if intermedValue <= value:
                    intermedValue = value
                    break
            newImage[row][col] = intermedValue
    return newImage
