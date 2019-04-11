# Automaticaly suggest a transform based upon the histogram
from .histogram import Hist


def suggest(image):
    hist = Hist(image).hist
    suggestion = None
    if testForEq(hist):
        suggestion = "equal"
    elif testForLog(hist):
        suggestion = "log"
    elif testForPowLaw(hist):
        suggestion = "power"
    
    return suggestion


# Histogram flattening/Equalization
# Idea - if the entire histogram is restricted to 66% of the range. This method should be suggested.
# Seems like a naive approach but it can be tested to see how it works out.
def testForEq(hist):
    min = 0
    max = 0
    forward = 0  # forward iterator
    backward = len(hist) - 1  # backward iterator
    while forward < len(hist):
        if hist[forward] != 0 and min == 0:
            min = forward
        if hist[backward] != 0 and max == 0:
            max = backward
        if min != 0 and max != 0:
            break
        forward += 1
        backward -= 1
    percent = (max-min)/(len(hist)-1)
    if percent <= 0.66:
        return True
    else:
        return False


# Logarithmic Transformation
# Idea - If the image max and min values span most of the range but is 
# concentrated primarily in the darker range
def testForLog(hist):

    return False 


# Power-Law (Gamma) Transform
def testForPowLaw(hist):

    return False