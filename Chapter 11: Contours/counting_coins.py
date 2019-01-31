#!/usr/bin/env python

from __future__ import print_function
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

edged = cv2.Canny(blurred, 30, 150)
# cv2.imshow("Edges", edged)

cv2.imshow("Edge Detection", np.hstack([gray, blurred, edged]))

(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count %d coins in this image" % (len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)

for (i, c) in enumerate (cnts):
    (x, y, w, h) = cv2.boundingRect(c)

    print("Coins #%d" % (i + 1))
    coin = image[y:y+h, x:x+w]
    cv2.imshow("Coin", coin)

    mask = np.zeros(image.shape[:2], dtype="uint8")

    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)

    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)

    mask = mask[y:y+h, x:x+w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask=mask))
    cv2.waitKey(0)
