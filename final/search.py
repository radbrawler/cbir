# import the necessary packages
from colordescriptor import ColorDescriptor
import numpy as np
from pyimagesearch.zernikemoments import ZernikeMoments
from HogDescriptor import HogDescriptor
from hu import ShapeDescriptor
from searcher import Searcher
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True,
	help="Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required=True,
	help="Path to the query image")
ap.add_argument("-r", "--result-path", required=True,
	help="Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
#cd = ShapeDescriptor()
#cd = ZernikeMoments(50)
cd = HogDescriptor()
#cd = ColorDescriptor()
# load the query image and describe it
query = cv2.imread(args["query"])
query = cv2.cvtColor(query, cv2.COLOR_BGR2GRAY)
	# pad the image with extra white pixels to ensure the
	# edges of the pokemon are not up against the borders
	# of the image
#query = cv2.copyMakeBorder(query, 15, 15, 15, 15,
#	cv2.BORDER_CONSTANT, value = 255)

	# invert the image and threshold it
#thresh = cv2.bitwise_not(query)
#thresh[thresh > 0] = 255

	# initialize the outline image, find the outermost
	# contours (the outline) of the pokemone, then draw
	# it
#outline = np.zeros(query.shape, dtype = "uint8")
#(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, 
#	cv2.CHAIN_APPROX_SIMPLE)
#cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
#cv2.drawContours(outline, [cnts], -1, 255, -1)

features = cd.describe_hog(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)

# display the query
cv2.imshow("Query", query)
print ("Reached here")

# loop over the results
for (score, resultID) in results:
	# load the result image and display it
	print (score)
	result = cv2.imread(args["result_path"] + "/" + resultID)
	cv2.imshow("Result", result)
	cv2.waitKey(0)
