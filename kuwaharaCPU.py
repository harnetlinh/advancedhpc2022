# create function RGB image to SHV image with numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
import math

# get the image
root = mpimg.imread('cute-cat.jpg')
imgplot = plt.imshow(root)
plt.show()
print("----------------------------------------")

# convert RGB image to HSV image with numpy and matplotlib
def rgb_to_hsv(src):
    height, width = src.shape[0], src.shape[1]
    dst = np.zeros((height, width, 3), dtype=np.uint8)
    for tidx in range(height):
        for tidy in range(width):
            b = src[tidx, tidy, 0] / 255
            g = src[tidx, tidy, 1] / 255
            r = src[tidx, tidy, 2] / 255
            cmax = max(r, g, b)
            cmin = min(r, g, b)
            delta = cmax - cmin
            if delta == 0:
                h = 0
            elif cmax == r:
                h = ((((g - b) / delta) % 6) * 60)  % 360
            elif cmax == g:
                h = ((((b - r) / delta) + 2) * 60) % 360
            elif cmax == b:
                h = ((((r - g) / delta) + 4) * 60) % 360
            if cmax == 0:
                s = 0
            else:
                s = delta / cmax
            v = cmax

            dst[tidx, tidy, 0] = h % 360
            dst[tidx, tidy, 1] = s * 100
            dst[tidx, tidy, 2] = v * 100

    return dst

# display HSV image
hsv = rgb_to_hsv(root)
imgplot = plt.imshow(hsv)
plt.show()