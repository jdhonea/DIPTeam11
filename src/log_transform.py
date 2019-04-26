import numpy as np
import cv2

class LogTransform:
    def log_transform(self, img, c):
        self.rows = img.shape[0] #number of rows
        self.columns = img.shape[1] #number of columns

        self.resulted_img = np.zeros(shape = img.shape)

        c = c/np.log(1+255)
        max = np.max(img)

        for i in range(self.rows):
            for j in range(self.columns):
                self.resulted_img[i,j] = c*(np.log(img[i,j] + 1) / (np.log(1 + max))) * 255


        return self.resulted_img

