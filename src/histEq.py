from .miscFuncts import displayImage


<<<<<<< HEAD
def histEqual(self, image, imageHist):
=======
def histEq(image, imageHist):
>>>>>>> 617969a690ec1b07538852cf7617af4b8dc41cce
    # Equalizes a histogram
    # Receives a source image and histogram
    # Returns altered image and histogram
    pdf = imageHist.pdf  # get PDF
    cdf = imageHist.cdf  # get CDF
    hist = imageHist.hist  # get histogram
<<<<<<< HEAD
    main.display_image("image", image)
=======
    displayImage("image", image)
>>>>>>> 617969a690ec1b07538852cf7617af4b8dc41cce
    return (image, imageHist)


'''
Steps:
1. Calculate Hist.
2. Calculate PDF
3. Calculate CDF
4. Multiply CDF with ((grey levels)-1) ie 255
5. 
'''