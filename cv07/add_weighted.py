import cv2

img1 = cv2.imread('ml.jpg')
img2 = cv2.imread('opencv_logo_1.png')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
