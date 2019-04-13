import numpy as np

def powerLaw(image, gamma):

    c = 255
    new_image = np.array(c*(image/c)**gamma , dtype=np.uint8)
    return new_image

