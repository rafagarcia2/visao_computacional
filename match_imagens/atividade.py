import numpy as np, math
from PIL import Image

I2 = Image.open('finn.png')
I2 = I2.convert('L')

I = Image.open('eleven2.jpg')
I = I.convert('L')


def passaaltaideal(image):
    a = np.asarray(image)
    A = np.fft.fft2(a)
    A = np.fft.fftshift(A)

    for u in range(image.size[0]):
        for v in range(image.size[1]):
            u1 = u - image.size[0]/2
            v1 = v - image.size[1]/2
            Duv = math.sqrt(u1*u1 + v1*v1)
            if Duv > 100:
                Huv = 1
            else:
                Huv = 0
            A[v][u] = Huv*A[v][u]

    
    Image.fromarray(abs(A)/800)

    return A

def passabaixaideal(image):
    a = np.asarray(image)
    A = np.fft.fft2(a)
    A = np.fft.fftshift(A)

    for u in range(image.size[0]):
        for v in range(image.size[1]):
            u1 = u - image.size[0]/2
            v1 = v - image.size[1]/2
            Duv = math.sqrt(u1*u1 + v1*v1)
            if Duv < 20:
                Huv = 1
            else:
                Huv = 0
            A[v][u] = Huv*A[v][u]

    Image.fromarray(abs(A)/800)

    return A

pbi = passabaixaideal(I)
pai = passaaltaideal(I2)

new_img = pbi + pai

new_img = Image.fromarray(np.abs(np.fft.ifft2(new_img)).astype(np.uint8))
new_img.show()
new_img.save("result.jpg")
