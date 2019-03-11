'''
1.  Através de uma implementação, aumente o brilho de uma imagem e pinte faixas pretas
    verticais em uma imagem para obter o seguinte efeito:
'''
import cv2
import numpy as np

alpha = 1.5     # Simple contrast control
beta = 70      # Simple brightness control

image_original = cv2.imread('nazare-confusa.jpg')

image = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

new_image = np.zeros(image.shape, image.dtype)

for y in range(image.shape[0]):
    black = True
    aux = 1
    for x in range(image.shape[1]):
        if (black and aux % 16 == 0) or (not black and aux % 8 == 0):
            black = not black
            aux = 1
        aux += 1
        if black:
            new_image[y,x] = np.clip(0, 0, 255)
        else:
            new_image[y,x] = np.clip(alpha*image[y,x] + beta, 0, 255)

print(new_image.shape)
cv2.imshow('R-RGB', new_image)

# Imprimindo a imagem
cv2.waitKey(0)