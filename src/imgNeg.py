import numpy as np
import cv2


def imgNegative(image):
    # Inputs image and returns a negative
    NegImage = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)

    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            # S (output pixel) = L (size) - 1 - r (input pixel)
            NegImage[i, j] = image.shape[0] - 1 - image[i, j]

    return NegImage