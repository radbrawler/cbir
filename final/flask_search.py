from colordescriptor import ColorDescriptor
import numpy as np
from pyimagesearch.zernikemoments import ZernikeMoments
from HogDescriptor import HogDescriptor
from hu import ShapeDescriptor
from searcher import Searcher
import argparse
import cv2

def flask_search(image):
	cd = HogDescriptor()
	# load the query image and describe it
	print (image)
	image = cv2.imread(image)
	image = (255 - image)
	image = cv2.resize(image, (256,256))
	query = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	features = cd.describe_hog(query)

	# perform the search
	# args['index'] is not defined
	searcher = Searcher('hog_index.csv')
	results = searcher.search(features)
	print (results)
	return results
	# display the query
	# cv2.imshow("Query", query)
	# print ("Reached here")
	# loop over the results
	# for (score, resultID) in results:
	# 	# load the result image and display it
	# 	result = cv2.imread(args["result_path"] + "/" + resultID)
	# 	path.extend(resultID)
	# 	#cv2.imshow("Result", result)
	# 	#cv2.waitKey(0)
	# return path
