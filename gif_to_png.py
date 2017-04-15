from PIL import Image
import os
import glob
import argparse

files = glob.glob("original/*.gif") 
for images in glob.glob("original" + "/*.gif"):
    imageID = images[images.rfind("/") + 1:]
    name = os.path.basename(images).split('.')[0]
    im = Image.open(imagePath)
    im.save(name+".png", 'PNG')
    im.thumbnail((10, 10))

