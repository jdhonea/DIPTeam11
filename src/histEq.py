#Only needed for demo and debugging
import cv2

#Equalizes a histogram
#Receives a source image and histogram
#Returns altered image and histogram
def histEq(self, image, imageHist):
    pdf = [] #get PDF
    cdf = [] #get CDF
    

    return (image, imageHist)

#hopefully these will get covered in a Histogram class or something
def getPDF(image):
    pdf = []
    return pdf

#hopefully these will get covered in a Histogram class or something
def getCDF(pdf):
    cdf = []
    return cdf

'''
Steps:
1. Calculate Hist.
2. Calculate PDF
3. Calculate CDF
4. Multiply CDF with ((grey levels)-1) ie 255
5. 
'''