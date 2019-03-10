'''
1.  Através de uma implementação, aumente o brilho de uma imagem e pinte faixas pretas
    verticais em uma imagem para obter o seguinte efeito:
'''


import cv2
import math
import numpy as np

alpha = 1.5     # Simple contrast control
beta = 10      # Simple brightness control

#image = cv2.imread('millenium_falcon.JPG') # save b, g, r
image = cv2.imread('luke_age.jpg')

new_image = np.zeros(image.shape, image.dtype)

for y in range(image.shape[0]):
    black = True
    aux = 1
    for x in range(image.shape[1]):
        if (black and aux % 16 == 0) or (not black and aux % 8 == 0):
            black = not black
            aux = 1
        aux += 1
        for c in range(image.shape[2]):
            if black:
                new_image[y,x,c] = np.clip(0, 0, 255)
            else:
                new_image[y,x,c] = np.clip(alpha*image[y,x,c] - beta, 0, 255)


print(new_image.shape)
cv2.imshow('R-RGB', new_image)

# Imprimindo a imagem
cv2.waitKey(0)