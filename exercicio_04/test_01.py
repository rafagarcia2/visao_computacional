'''
1.  Através de uma implementação, aumente o brilho de uma imagem e pinte faixas pretas
    verticais em uma imagem para obter o seguinte efeito:
'''
import cv2
import numpy as np

alpha = 1.5     # Simple contrast control
beta = 70      # Simple brightness control

image_original = cv2.imread('laranjas.jpg')

image = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

new_image = np.zeros(image.shape, image.dtype)

for y in range(image.shape[0]):
    black = True
    for x in range(image.shape[1]):
        if image[y, x] < 127:
            new_image[y,x] = np.clip(0, 0, 255)
        else:
            new_image[y,x] = np.clip(image[y,x], 0, 255)

# show image
cv2.imshow('R-RGB', new_image)
cv2.waitKey(0)