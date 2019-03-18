import numpy
from PIL import Image

I = Image.open('a_r2d2.jpg')
I = I.convert('L')


def passaaltaideal(image):
    a = numpy.asarray(image)
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

    res = numpy.multiply(S, A)

    new_image = Image.fromarray(numpy.fft.ifft2(res).astype(numpy.uint8))

    return new_image

r = passaaltaideal(I)
r.show()
#print(r)
print(type(r))