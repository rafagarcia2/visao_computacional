import numpy
from PIL import Image

I = Image.open('a_r2d2.jpg')
I = I.convert('L')
a = numpy.asarray(I)

filtro = numpy.zeros(a.shape)
a.flags.writeable = True
filtro.flags.writeable = True

#filtro da media tamanho M por M
M = 20
for i in range(M):
	for j in range(M):
		filtro[i][j] = 1.0/(M*M)

S = numpy.fft.fft2(filtro)
A = numpy.fft.fft2(a)

print (S)