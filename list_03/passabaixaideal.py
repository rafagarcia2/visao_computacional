import numpy, math
from PIL import Image
import cv2

I = Image.open('a_r2d2.jpg')
I = I.convert('L')
a = numpy.asarray(I)
A = numpy.fft.fft2(a)
A = numpy.fft.fftshift(A)

for u in range(I.size[0]):
	for v in range(I.size[1]):
		u1 = u - I.size[0]/2
		v1 = v - I.size[1]/2
		Duv = math.sqrt(u1*u1 + v1*v1)
		if Duv < 20:
			Huv = 1
		else:
			Huv = 0
		A[v][u] = Huv*A[v][u]

Image.fromarray(abs(A)/800).show()
A = numpy.fft.fftshift(A)

output = Image.fromarray(numpy.fft.ifft2(A).astype(numpy.uint8))
output.show()

cv2.imwrite('p_baixa_ideal.jpg', output)

