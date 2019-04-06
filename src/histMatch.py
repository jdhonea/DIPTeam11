from .histogram import Hist
import numpy as np


def histMatch(image, target):
    # Receives an image and a target image
    # Returns image and histogram
    imageHist = Hist(image)
    targetHist = Hist(target)
    imgCDF = imageHist.cdf
    targetCDF = targetHist.cdf
    imgCDF = [int(x * 255) for x in imgCDF]
    targetCDF = [int(x * 255) for x in targetCDF]
    image = calculateImage(image, imgCDF, targetCDF)
    newHist = Hist(image).hist
    return (image, newHist)


def calculateImage(image, src, target):
    newImage = np.zeros(image.shape, np.uint8())
    for row in range(0, newImage.shape[0]):
        for col in range(0, newImage.shape[1]):
            intermedValue = src[image[row][col]]  # Grabs the CDF value from the src image
            for index, value in enumerate(target):
                # Matches the CDF value to that in the target CDF
                if intermedValue <= value:
                    intermedValue = index
                    break
            newImage[row][col] = intermedValue
    return newImage
