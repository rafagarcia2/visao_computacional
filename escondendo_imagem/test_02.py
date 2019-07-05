import cv2
import numpy as np 

image = cv2.imread("lena_escondida.jpg")

# load 
src_h, src_w, _ = image.shape

#average filter
sizef = 15
average_filter = np.ones((sizef,sizef), dtype=np.float32)
for i in range(sizef):
	for j in range(sizef):
		average_filter[i,j] = 1./float(sizef*sizef)

#smoothing image
soma = 0
for i in range (image.shape[1] - sizef):
	for j in range (image.shape[0] - sizef):
		for k in range (sizef):
			for f in range(sizef):
				soma = soma + average_filter[k,f] * image[i+k, j+f]
		center = int(sizef/2) + 1
		image[i+center, j+center] = soma
		soma = 0

avr = cv2.filter2D(image, -1, average_filter)

# plot image
cv2.imwrite("suave1.jpg", image)
cv2.imwrite("suave2.jpg", avr)