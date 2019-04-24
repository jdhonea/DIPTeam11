import numpy as np

class LogTransform:
    def log_transform(self, image, c):
        self.rows = image.shape[0] #number of rows
        self.columns = image.shape[1] #number of columns

        self.resulted_img = np.zeros(shape = image.shape)

        for i in range(self.rows):
            for j in range(self.columns):
                self.resulted_img[i,j] = c*np.log(image[i,j] + 1)


        return self.resulted_img