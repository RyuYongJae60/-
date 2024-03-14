import os
import cv2
import numpy as np
import math

os.chdir(os.path.dirname(os.path.abspath(__file__)))

img_origin = cv2.imread("fish.png",0)
rows, cols = img_origin.shape   # rows: h, cols: w

theta = 0

while True:
    radian = math.radians(theta)
    
    w_ = cols * abs(math.cos(radian)) + rows * abs(math.sin(radian))
    h_ = cols * abs(math.sin(radian)) + rows * abs(math.cos(radian))
    
    rotaion_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), theta, 1)
    M = np.array(rotaion_matrix)
    M[0, 2] = M[0,2] + (w_/2 - cols/2)
    M[1, 2] = M[1,2] + (h_/2 - rows/2)

     
    img_res = cv2.warpAffine(img_origin, M, (int(w_), int(h_)))
    
    cv2.imshow("", img_res)
    key = cv2.waitKey(0)

    if key == 27:   # ESC
        break

    if key == 32:
        if theta == 360:
            break

        theta += 10
        cv2.destroyAllWindows()


cv2.destroyAllWindows()

