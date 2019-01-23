#!/usr/bin/env python
import numpy as np
import cv2

# create an empty canvas(black)
canvas = np.zeros((300, 300, 3), dtype="uint8")

# initialize color
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)

# initialize center of canvas
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

# draw a line from (0, 0) to (300, 300) with green
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a line from (300, 0) to (0, 300) with red and thickness set at 3
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a rectangle start at (10, 10) end at (60, 60) with green
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a rectangle start at (50, 200) end at (200, 225) with red and thickness set at 5
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a rectangle start at (200, 50) end at (225, 125) with red and filled
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a circle in a range with white color
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a circle in a randomnese -- color, radius, center
for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
