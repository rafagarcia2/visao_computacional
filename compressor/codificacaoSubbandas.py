import cv2, numpy, scipy.ndimage.filters as sp

img = cv2.imread('lena.png', 0)
img = img.astype(numpy.float32)

#coeficientes do filtro ortonormal de Daubechies
g0 = [0.23037781, 0.71484657, 0.63088076, -0.02798376, -0.18703481, 0.03084138, 0.032288301, -0.01059740]
g1 = []
for i in range(0, len(g0)):
    if i%2 == 0:
        g1.append(g0[len(g0)-1-i])
    else:
        g1.append(-g0[len(g0)-1-i])

h1 = []
h0 = []
for i in range(0, len(g0)):
    h0.append(g0[len(g0)-1-i])
    h1.append(g1[len(g0)-1-i])

img2 = sp.convolve1d(img, h0, 0)[::2,::]
img3 = sp.convolve1d(img, h1, 0)[::2,::]
imga = sp.convolve1d(img2,h0, 1)[::,::2]
imgv = sp.convolve1d(img2,h1, 1)[::,::2]
imgh = sp.convolve1d(img3,h0, 1)[::,::2]
imgd = sp.convolve1d(img3,h1, 1)[::,::2]

#m = sub-banda a ser exibida
m = imga
m = m - m.min()
m = 255*m/m.max() 

cv2.imshow('janela', m.astype(numpy.uint8))
cv2.waitKey(0)
