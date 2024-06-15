import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
np.set_printoptions(4,suppress=True)


def cv2_imshow(imgz, title=None, cmap='gray'):
    plt.imshow(imgz, cmap=cmap)
    if title is not None:
        plt.title(title)
    plt.show()
    
image = cv2.imread("house1.png", 0)
print("im shape:",image.shape)
print("im dim:",image.ndim)
cv2_imshow(image, "Canny Image")

image = cv2.imread("house2.png", 0)
print("im shape:",image.shape)
print("im dim:",image.ndim)
cv2_imshow(image, "Canny Image")