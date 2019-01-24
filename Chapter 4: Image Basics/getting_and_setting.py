#!/usr/bin/env python
from __future__ import print_function
import argparse
import cv2

# argument parse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
# cloning an image
imageClone = image.copy()

# analyzing image
(b, g, r) = imageClone[0, 0]
print("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))

# manipulating image
imageClone[0, 0] = (0, 0, 255)
(b, g, r) = imageClone[0, 0]
print("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))

# slicing image
corner = imageClone[0:100, 0:100]
cv2.imshow("Corners", corner)

# manipulating an image
imageClone[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Manipulated", imageClone)

# display image
cv2.imshow("Image", image)
cv2.waitKey(0)
