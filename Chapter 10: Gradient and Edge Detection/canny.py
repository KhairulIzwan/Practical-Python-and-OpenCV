#!/usr/bin/env python

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

gray = image.copy()
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grayscale", gray)

blurred = cv2.GaussianBlur(gray, (11, 11), 0)
# cv2.imshow("Blurred", blurred)

canny = cv2.Canny(blurred, 30, 120)
# cv2.imshow("Canny", canny)

cv2.imshow("Edge Detection", np.hstack([gray, blurred, canny]))

cv2.waitKey(0)
