import numpy as np
from .histogram import Hist


def histEq(image):
    # Equalizes a histogram
    # Receives a source image and histogram
    # Returns altered image and histogram
    histogram = Hist(image)
    cdf = histogram.cdf  # get CDF
    hist = histogram.hist  # get histogram
    cdf = [int(x * 255) for x in cdf]
    image = equalized(image, cdf)
    hist = Hist(image)
    newHist = hist.hist
    return (image, newHist)


def equalized(src, cdf):
    image = np.zeros(src.shape, np.uint8())
    for row in range(0, image.shape[0]):
        for col in range(0, image.shape[1]):
            pixelValue = src[row][col]
            image[row][col] = cdf[pixelValue]
    return image