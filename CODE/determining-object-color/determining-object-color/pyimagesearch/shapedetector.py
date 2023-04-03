# import the necessary packages
import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		widthheightdimensions = []
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)
		(x, y, w, h) = cv2.boundingRect(approx)

		#print(w)
		#print(h)
		if (w > 20 and h > 20 and w<250 and h<250):

			# if the shape has 4 vertices, it is either a square or
			# a rectangle
			if len(approx) == 4:
				# compute the bounding box of the contour and use the
				# bounding box to compute the aspect ratio
				ar = w / float(h)
				widthheightdimensions = [w, h]
				# a square will have an aspect ratio that is approximately
				# equal to one, otherwise, the shape is a rectangle
				shape =  "rectangle"



			# return the name of the shape
		return shape, widthheightdimensions