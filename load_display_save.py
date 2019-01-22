#!/usr/bin/env python
from __future__ import print_function
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image (read)")
ap.add_argument("-f", "--filename", required=True, help="Path to the image (save)")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])

# analyzing image
rows, columns, channels = image.shape
print("Height: %d" % rows)
print("Width: %d" % columns)
print("Channels: %d" % channels)

# display image
cv2.imshow("Image", image)
cv2.waitKey(0)

# save image
cv2.imwrite(args["filename"], image)
