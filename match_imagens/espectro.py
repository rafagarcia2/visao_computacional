import numpy
from PIL import Image

I = Image.open('a_r2d2.jpg')
I = I.convert('L')
a = numpy.asarray(I)
A = numpy.fft.fft2(a)

#centralizando o espectro
A = numpy.fft.fftshift(A)

#os valores do espectro sao divididos por 800 para fins de visualizacao
output = Image.fromarray(abs(A)/800)
output.show()
