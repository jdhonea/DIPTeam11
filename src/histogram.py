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


   #==================Histogram Shaping===================
    def binary_search(self,lis, key): #make HistShap function run faster
        low = 0
        high = len(lis) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if key < lis[mid] and key < lis[mid-1] and mid!=0:
                high = mid - 1
            elif key > lis[mid] and key>lis[mid+1] and mid!=255:
                low = mid + 1
            elif key > lis[mid] and key < lis[mid+1] and mid!=255:
                return mid+1
            else:
                return mid
    def app_spec_hist(self):  #create a approximate specified histogram shape, this is work with HistShap function
        j=255
        Bell = [0 for i in range(256)]
        for i in range(0,128):
            Bell[i]=i*2
            Bell[j]=i*2
            j=j-1

        bimodal= [0 for i in range(256)]
        a=0
        for i in range(0, 256):
            if i>=0 and i<80:
                bimodal[i]=a
                a=a+2
            elif i>=80 and i<128:
                bimodal[i]=a
                a=a-2
            elif i >= 128 and i < 176:
                bimodal[i] = a
                a=a+2
            elif i>=176   and i<256:
                bimodal[i]=a
                a=a-2
        a=0
        rightSk=[0 for i in range(256)]
        for i in range(0, 256):
            if i >= 0 and i < 50:
                rightSk[i] = a
                a=a+10
            else:
                rightSk[i] = a
                a=a-500/206

        Jshaped=[0 for i in range(256)]
        a=512
        for i in range(0, 256):
            Jshaped[i]=a
            a=a-2

        Ushaped=[0 for i in range(256)]
        a=800
        for i in range(0, 256):
            if i >= 0 and i < 128:
                Ushaped[i] = a
                a = a -6
            else:
                Ushaped[i] = a
                a = a +6
        return [Bell,bimodal,rightSk,Jshaped,Ushaped]

    #this is histogram shaping function ,return to a processed image
    # hist.HistShap(hist.app_spec_hist()[0])=bell shaped
    # hist.HistShap(hist.app_spec_hist()[1])=bimodal shaped
    # hist.HistShap(hist.app_spec_hist()[2])=Right skewed
    # hist.HistShap(hist.app_spec_hist()[3])=J shaped
    # hist.HistShap(hist.app_spec_hist()[4])=U shaped
    def HistShap(self, app_spec_hist):
        histogram = Hist(self.image)
        J1=histogram.uniform()[1]            #get Pj(k)
        probabilities = [0 for i in range(256)]
        j=3
        sum=0
        for i in range(0, 256):
            sum= sum + app_spec_hist[i]
        for i in range(0, 256):
            app_spec_hist[i]= app_spec_hist[i] / sum
        probabilities=app_spec_hist
        for i in range(0, 256):
            if i>0 and i!=255:
                probabilities[i] = probabilities[i-1]+ probabilities[i]  # Here's the cumulative (summed) probabilities associated
            elif i==255:
                probabilities[i]=1                                      #last one should be 100%,in some case the result show 0.999999......
        Newimage = np.zeros(self.image.shape, np.uint8())
        for row in range(0, Newimage.shape[0]):
            for col in range(0, Newimage.shape[1]):
                Newimage[row][col]=histogram.binary_search(probabilities,J1[row][col])
        return Newimage
    #uniform is different frome other 5 histshape So need a independent function
    #uniform[0] is return to processed image
    def uniform(self):
        histogram = Hist(self.image)
        hist = histogram.hist  # get histogram
        sum=self.image.shape[0]*self.image.shape[1]  #get total number of pixel
        for i in range(0, 256):
            hist[i]=hist[i]/sum         #P for every pixel
        for i in range(0, 256):
            if i>0:
                hist[i] =hist[i-1]+hist[i]  #now hist = Pj(k)
        Newimage = np.zeros(self.image.shape, np.uint8())
        J1 = np.zeros((self.image.shape[0], self.image.shape[1]), dtype=np.float)
        for row in range(0, Newimage.shape[0]):
            for col in range(0, Newimage.shape[1]):
                J1[row][col] =hist[self.image[row][col]]
                Newimage[row][col]=J1[row][col]*255
                #print(Newimage[row][col])

        return [Newimage,J1]     #Newimage is image processing for uniform
