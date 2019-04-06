from .histogram import Hist


def histMatch(image, target):
    # Receives an image and a target image
    # Returns image and histogram
    hist = []
    imageHist = Hist(image)
    targetHist = Hist(target)

    return (image, hist)
