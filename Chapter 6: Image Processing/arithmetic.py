#!/usr/bin/env python
from __future__ import print_function
import argparse
import cv2
import numpy as np

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image (read)")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])

# display image
cv2.imshow("Image", image)
cv2.waitKey(0)

print("max of 255: %d" % (cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 255: %d" % (cv2.subtract(np.uint8([50]), np.uint8([100]))))
print("wrap around: %d" % (np.uint8([200]) + np.uint8([100])))
print("wrap around: %d" % (np.uint8([50]) - np.uint8([100])))

M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

M = np.ones(image.shape, dtype="uint8") * 50
subtract = cv2.subtract(image, M)
cv2.imshow("Subtract", subtract)
cv2.waitKey(0)
