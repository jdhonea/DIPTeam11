import cv2
import numpy as np

class Hist:
    def __init__(self, image):
        self.image = image
        self.hist = self.calculateHist()
        self.pdf = self.calculatePDF()
        self.cdf = self.calculateCDF()
    
    def calculateHist(self):
        hist = [0] * 256
        for row in range(0, self.image.shape[0]):
            for col in range(0, self.image.shape[1]):
                hist[self.image[row][col]] += 1
        return hist

    def calculatePDF(self):
        pdf = [0] * 256
        sizeOfImage = self.image.shape[0] * self.image.shape[1]
        for x in range(0, len(pdf)):
            pdf[x] = self.hist[x]/sizeOfImage
        
        return pdf

    def calculateCDF(self):
        cdf = [0] * 256
        sum = 0
        for x in range(0,len(self.pdf)):
            sum += self.pdf[x]
            cdf[x] = sum
        return cdf

