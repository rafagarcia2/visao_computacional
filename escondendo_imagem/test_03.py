
import cv2
import math
import numpy as np

#image = cv2.imread('millenium_falcon.JPG') # save b, g, r
image = cv2.imread('luke_age.jpg')

new_image = np.zeros(image.shape, image.dtype)

for y in range(1, 5): # image.shape[0]-1):
    black = True
    mean = 0
    for x in range(1, 5): # image.shape[1]-1):
        kernel = image[y-1:y+2, x-1:x+2]
        print(kernel)
        print(image[y][x])

print(new_image.shape)
# cv2.imshow('R-RGB', new_image)

# Imprimindo a imagem
# cv2.waitKey(0)