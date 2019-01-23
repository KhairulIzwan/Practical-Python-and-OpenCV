#!/usr/bin/env python
from matplotlib import pyplot as plt
import argparse
import cv2

# argument parser`
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# original image
image = cv2.imread(args["image"])
imageClone = image.copy()

imageClone = cv2.cvtColor(imageClone, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", imageClone)

hist = cv2.calcHist(imageClone, [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
