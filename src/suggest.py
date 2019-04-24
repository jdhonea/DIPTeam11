from .histogram import Hist
import numpy as np
import matplotlib.pyplot as plt


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
    elif testForPowLaw(histogram):
        suggestion = "power"
    elif testForLog(histogram):
        suggestion = "log"
    else:
        return "none"
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
# TODO: Figure out a better way to test for this transformation!
# Idea - If the intensity values of the image expand more than 66% of the image,
# but is mostly concentrated in the dark region. A better test should be 
# thought of.
def testForLog(hist):
    cdf = hist.cdf
    if cdf[80] >= 0.70:
        return True
    else:
        return False


# Power-Law (Gamma) Transform
# TODO: Figure out a way to test for this transformation!
def testForPowLaw(hist):
    # Steps:
    # 1. Get the cdf
    # 2. Calculate current gamma curve for gamma x on ranges 0 - 255
    # 3. Find the |distance| between the gamma curve and the image cdf, smaller the value the more similar the curves are
    # 4. If the curve falls within a certain threshold of similarity, gamma transform should be recommended.
    hist = hist.cdf
    hist = [int(x * 255) for x in hist]
    gammaOffset = .5  # Offset to be added to the gamma values to increment them along
    normalHist = np.arange(256)
    lowerGamma = 0
    while (lowerGamma < 25):
        upperSum = 0
        lowerSum = 0
        upperGamma = 1/(1 + gammaOffset)  # The curve related to 1/x
        lowerGamma = 1 + gammaOffset  # The curve related to x
        upperCurve = np.array(255*(normalHist/255)**upperGamma)  # Generate the upper curve
        lowerCurve = np.array(255*(normalHist/255)**lowerGamma)  # Generate the lower curve
        for i in range(0, len(hist), 3):  # Summation every 3 steps
            upperSum += abs(upperCurve[i] - hist[i])
            lowerSum += abs(lowerCurve[i] - hist[i])
        if upperSum < 2500:
            print(upperGamma)
            """plt.plot(hist)
            plt.plot(upperCurve)
            plt.show()"""
            return True
        elif lowerSum < 2500:
            print(lowerGamma)
            return True
        gammaOffset += .5
        # print("Upper Curve:", upperSum, "Lower Curve:", lowerSum)
    return False
