'''
3. Escreva um programa para:
    (a) abrir uma imagem e exibir na tela os 3 canais separadamente
'''


import cv2
import numpy

img = cv2.imread('r2d2.jpg') # save b, g, r

b,g,r = cv2.split(img)
image = cv2.merge((r, g, b))

#RGB - Blue
b = image.copy()
# canais G e R iguais a 0
b[:, :, 1:3] = 0
cv2.imshow('B-RGB.jpg', b)
#cv2.imwrite('B-RGB.jpg',b)

# RGB - Green
g = image.copy()
# canais G e R iguais a 0
g[:, :, 0] = 0
g[:, :, 2] = 0
# cv2.imshow('G-RGB', g)
# cv2.imwrite('G-RGB.jpg',g)

# RGB Red
r = image.copy()
# canais G e R iguais a 0
r[:, :, 0:2] = 0
# cv2.imshow('R-RGB', r)
# cv2.imwrite('R-RGB.jpg', r)


# Imprimindo a imagem
cv2.waitKey(0)

print(b)
