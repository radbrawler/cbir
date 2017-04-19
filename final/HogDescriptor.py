import cv2
import matplotlib.pyplot as plt

import numpy as np

from skimage.feature import hog
from skimage import data, color, exposure

class HogDescriptor:
	def describe_hog(self, image):
		image = color.rgb2gray(image)	

		fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualise=True)
		return fd


