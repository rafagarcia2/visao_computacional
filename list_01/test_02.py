'''
3. Escreva um programa para:
    (a) abrir uma imagem e exibir na tela os 3 canais separadamente
'''


import cv2
import numpy

img = cv2.imread('r2d2.jpg') # save b, g, r

# Invertendo a lista
invertida = img[:, ::-1]

# Imprimindo a imagem
cv2.imshow('Invertida', invertida)
cv2.imwrite('Invertida.jpg', invertida)
cv2.waitKey(0)
