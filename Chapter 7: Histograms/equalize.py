#!/usr/bin/env python
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.waitKey(0)

equ = cv2.equalizeHist(image)
cv2.imshow("Histogram Equalization", equ)
cv2.waitKey(0)

cv2.imshow("Histogram Equalization", np.hstack([image, equ]))
cv2.waitKey(0)
