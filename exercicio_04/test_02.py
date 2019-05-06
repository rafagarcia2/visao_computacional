'''
1.  Através de uma implementação, aumente o brilho de uma imagem e pinte faixas pretas
    verticais em uma imagem para obter o seguinte efeito:
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

alpha = 1.5     # Simple contrast control
beta = 70      # Simple brightness control

image_original = cv2.imread('laranjas.jpg')

image = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

_, new_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU )

kernel = np.ones((6, 6),np.uint8)
kernel2 = np.ones((5, 5),np.uint8)

opening = cv2.morphologyEx(new_image, cv2.MORPH_OPEN, kernel)

dilation = cv2.dilate(opening, kernel, iterations = 1)

dilation2 = cv2.dilate(opening, kernel, iterations = 2)

closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel2)

# erosion = cv2.erode(dilation, kernel, iterations = 1)

cv2.imshow('Gray image', dilation2)
cv2.waitKey(0)
cv2.imshow('Gray image', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()