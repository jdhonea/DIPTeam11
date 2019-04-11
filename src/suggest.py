from .histogram import Hist


# Automaticaly suggest a transform based upon the histogram
# Tests for Histogram Equalization, Log Transformation, Power-Law (Gamma) Transformation
# TODO: Test constraints need to be tested and adjusted and there are probably better tests
# that can be implemented
def suggest(image):
    histogram = Hist(image)
    hist = histogram.hist
    suggestion = None
    if testForEq(hist):
        suggestion = "equal"
    elif testForLog(histogram):  # Equalization failed at this point, therefore histogram is not limited to 66% of range
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
# TODO: Figure out a a test for this transformation
def testForLog(hist):

    return False


# Power-Law (Gamma) Transform
# TODO: Figure out a way to test for this transformation
def testForPowLaw(hist):

    return False
