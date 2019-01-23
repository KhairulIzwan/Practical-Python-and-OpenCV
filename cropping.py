#!/usr/bin/env python
import numpy as np
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

cropped = image[63:270, 53:273]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
