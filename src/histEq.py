

def histEqual(self, image, imageHist):
    # Equalizes a histogram
    # Receives a source image and histogram
    # Returns altered image and histogram
    pdf = imageHist.pdf  # get PDF
    cdf = imageHist.cdf  # get CDF
    hist = imageHist.hist  # get histogram
    main.display_image("image", image)
    return (image, imageHist)


'''
Steps:
1. Calculate Hist.
2. Calculate PDF
3. Calculate CDF
4. Multiply CDF with ((grey levels)-1) ie 255
5. 
'''