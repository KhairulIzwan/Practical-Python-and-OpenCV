#!/usr/bin/env python
import argparse
import cv2

# argument parser`
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# flipped horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)

# flipped vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey(0)

# flipped vertically and horizontally
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Vertically and Horizontally", flipped)
cv2.waitKey(0)
