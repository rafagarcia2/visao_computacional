'''
3. Escreva um programa para:
    (a) abrir uma imagem e exibir na tela os 3 canais separadamente
'''


import cv2
import numpy as np

# save b, g, r
a = cv2.imread('a_r2d2.jpg') 
b = cv2.imread('b_bb8.png')

# Somando as duas imagens
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j])
        print(b[i][j])
        c = (0.5*a[i][j]) + (0.5*b[i][j])
        print(c)
        break

# Imprimindo a imagem
cv2.imshow('Merge', c)
cv2.imwrite('Merge.jpg', c)
cv2.waitKey(0)
