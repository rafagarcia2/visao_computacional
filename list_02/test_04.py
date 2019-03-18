import cv2
import numpy as np 

def filter_img(img, m_filter, sizef):
   
	# Sobel's filter
	vert_sobel_filter = np.array([[-1,0,1],[-2,0,2], [-1,0,1]], dtype=np.float32)

	# borders
	border = cv2.filter2D(img, -1, vert_sobel_filter)
	b,g,r = cv2.split(border)

	soma = 0
	for i in range (img.shape[1]-sizef):
		for j in range (img.shape[0]-sizef):
			for k in range (sizef):
				for f in range(sizef):
					soma = soma + m_filter[k,f] * img[i+k, j+f]
			
			c = sizef/2 + 1

			if b[i+c, j+c] > 10 and g[i+c, j+c] > 10 and r[i+c, j+c] >10:
				img[i+c,j+c] = soma			
			soma = 0

	return img


img = cv2.imread("r2d2.jpg")

size = 9
average_filter = np.ones((size,size), dtype=np.float32)
for i in range(size):
	for j in range(size):
		average_filter[i,j] = 1./float(size*size)

suv = filter_img(img, average_filter, size)

suv.show()
#cv2.imwrite("luke_2.jpg", suv)