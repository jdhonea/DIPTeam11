import numpy as np


def contrast_str(image):
    x = len(image[1])  # get number of row
    y = len(image)  # get number of cul
    Imax = np.max(image)  # get max pixel
    Imin = np.min(image)  # get min pixel
    rate = 255 / (Imax - Imin)
    transfor_matrix = np.zeros(image.shape)
    for i in range(0, int(y)):
        for j in range(0, int(x)):
            transfor_matrix[i, j] = round(rate * (image[i, j] - Imin))
    return transfor_matrix
