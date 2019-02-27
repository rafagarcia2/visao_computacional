'''
1.  Através de uma implementação, aumente o brilho de uma imagem e pinte faixas pretas
    verticais em uma imagem para obter o seguinte efeito:
'''


import cv2
import math
import numpy as np

def deroGauss(w=5,s=1,angle=0):
    wlim = (w-1)/2
    y,x = np.meshgrid(np.arange(-wlim,wlim+1),np.arange(-wlim,wlim+1))
    G = np.exp(-np.sum((np.square(x),np.square(y)),axis=0)/(2*np.float64(s)**2))
    G = G/np.sum(G)
    dGdx = -np.multiply(x,G)/np.float64(s)**2
    dGdy = -np.multiply(y,G)/np.float64(s)**2

    angle = angle*math.pi/180 #converting to radians

    dog = math.cos(angle)*dGdx + math.sin(angle)*dGdy

    return dog

def nonmaxsup(I,gradang):

    dim = I.shape
    Inms = np.zeros(dim)
    weak = np.zeros(dim)    
    strong = np.zeros(dim)
    final = np.zeros(dim)
    xshift = int(np.round(math.cos(gradang*np.pi/180)))
    yshift = int(np.round(math.sin(gradang*np.pi/180)))
    Ipad = np.pad(I,(1,),'constant',constant_values = (0,0))
    for r in xrange(1,dim[0]+1):
        for c in xrange(1,dim[1]+1):
            maggrad = [Ipad[r-xshift,c-yshift],Ipad[r,c],Ipad[r+xshift,c+yshift]]
            if Ipad[r,c] == np.max(maggrad):
                Inms[r-1,c-1] = Ipad[r,c]
    return Inms

img = cv2.imread('r2d2.jpg') # save b, g, r

b,g,r = cv2.split(img)
image = cv2.merge((r, g, b))

cv2.imshow('R-RGB', img)

# Imprimindo a imagem
cv2.waitKey(0)

print(b)
