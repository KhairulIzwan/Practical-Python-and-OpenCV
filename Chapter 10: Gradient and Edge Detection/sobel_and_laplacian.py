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
cv2.imshow("Grayscale", gray)

lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)

sobelX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("SobelX", sobelX)
cv2.imshow("SobelY", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)

cv2.waitKey(0)
