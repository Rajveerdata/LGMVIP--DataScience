import cv2

image = cv2.imread('3.jpeg')
grey_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Fixed the typo in COLOR_BGR2GRAY
invert = cv2.bitwise_not(grey_filter)  # Fixed the typo in bitwise_not
blur = cv2.GaussianBlur(invert, (21, 21), 0)  # Fixed the typo in GaussianBlur
invertedblur = cv2.bitwise_not(blur)

sketch_filter = cv2.divide(grey_filter, invertedblur, scale=256.0)
cv2.imwrite('output3.png', sketch_filter)

