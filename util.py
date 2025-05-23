import numpy as np
import cv2

def get_limits(color):
    c = np.unit8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimits = hsvC[0][0][0] - 10, 100, 100
    upperLimits = hsvC[0][0][0] + 10, 255, 255

    