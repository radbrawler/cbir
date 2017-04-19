
# import the necessary packages
import numpy as np
import cv2
import argparse

class ShapeDescriptor:
	def describe1(self, image):
		#  convert it to grayscale, and display it
		#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
		#cv2.imshow("image", image)
		# extract Hu Moments from the image -- this list of numbers
		# is our 'feature vector' used to quantify the shape of the
		# object in our image
		features = cv2.HuMoments(cv2.moments(image)).flatten()
		# return the feature vector
		return features

	