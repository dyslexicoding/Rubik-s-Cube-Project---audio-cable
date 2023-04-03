# USAGE
# python detect_color.py --image example_shapes.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
from pyimagesearch.colorlabeler import ColorLabeler
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to the input image")
#args = vars(ap.parse_args())
def run(image):
	# load the image and resize it to a smaller factor so that
	# the shapes can be approximated better
	#image = cv2.imread(r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\real1.jpg')
	#image = cv2.resize(image, (300, 300))
	resized = imutils.resize(image, width=300)
	ratio = image.shape[0] / float(resized.shape[0])

	# blur the resized image slightly, then convert it to both
	# grayscale and the L*a*b* color spaces
	blurred = cv2.GaussianBlur(resized, (5, 5), 0)
	gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
	lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
	thresh = cv2.threshold(gray,100, 255, cv2.THRESH_BINARY)[1]
	cv2.imshow("Thresh", thresh)

	# find contours in the thresholded image
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	faceletnumber = 0
	# initialize the shape detector and color labeler
	sd = ShapeDetector()
	cl = ColorLabeler()
	faceletarray = []
	cXarray = []
	cYarray = []
	# loop over the contours
	for c in cnts:
		# compute the center of the contour
		M = cv2.moments(c)
		x = M["m00"]
		if (x > 0):
			cX = int((M["m10"] / M["m00"]) * ratio)
			cY = int((M["m01"] / M["m00"]) * ratio)

			# detect the shape of the contour and label the color
			(shape, widthheight) = sd.detect(c)
			color = cl.label(lab, c)

			if (shape == 'rectangle'):
				faceletnumber = faceletnumber+1
				facelet = [faceletnumber, cX, cY, widthheight[0], widthheight[1]]
				cXarray.append(cX)
				cYarray.append(cY)
				faceletarray.append(facelet)
				# multiply the contour (x, y)-coordinates by the resize ratio,
				# then draw the contours and the name of the shape and labeled
				# color on the image
				c = c.astype("float")
				c *= ratio
				c = c.astype("int")
				text = "{} {}".format(color, shape)
				cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

				# show the output image
				cv2.imshow("Image", image)
	print(faceletarray)
	cv2.waitKey(0)

	return (faceletarray, cXarray, cYarray)

