import cv2
# Created to house miscellaneous functions that will be useful.
# Storing in main creates a bit of a headache due to circular import statements
# and this seems like a much easier solution.


# DEBUGGING ONLY
def displayImage(window_name, image):
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()