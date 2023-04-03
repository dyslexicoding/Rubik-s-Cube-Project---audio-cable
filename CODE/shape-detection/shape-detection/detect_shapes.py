# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2



# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread(r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\1.jpg')
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 40, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("thresh", thresh)

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()
faceletarray = []
# loop over the contours
shapenumber = 0
for c in cnts:
	print (c)
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	M = cv2.moments(c)
	x = M["m00"]
	if (x>0):
		cX = int((M["m10"] / M["m00"]) * ratio)
		cY = int((M["m01"] / M["m00"]) * ratio)
		shape = sd.detect(c)
		if (shape == 'rectangle'):
			shapenumber=shapenumber+1
			facelet = [shapenumber, cX, cY]
			faceletarray.append(facelet)

			# multiply the contour (x, y)-coordinates by the resize ratio,
			# then draw the contours and the name of the shape on the image
			c = c.astype("float")
			c *= ratio
			c = c.astype("int")
			cv2.drawContours(image, [c], -1, (0, 255, 0), 2)


			# show the output image
			cv2.imshow("Image", image)
print(shapenumber)
print(faceletarray)
cv2.waitKey(0)