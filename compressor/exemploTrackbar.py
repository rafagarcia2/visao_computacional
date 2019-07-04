import cv2

img = cv2.imread('lena.jpg', 0)
windowName = 'janela'
thresholdLabel = 'Limiar'

def nothing(x):
	pass

cv2.namedWindow(windowName)
cv2.createTrackbar(thresholdLabel, windowName, 0, 255, nothing)

while True:
	threshold = cv2.getTrackbarPos(thresholdLabel, windowName)
	print threshold
	_,img2 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
	cv2.imshow(windowName, img2)
	key = cv2.waitKey(1)
	if key == 27:
		break

cv2.destroyAllWindows()
