import os
import cv2
import numpy as np
import math

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image as grayscale
img_orig = cv2.imread('fish.png', 0)
rows,cols = img_orig.shape  # w: cols, h: rows
#print(cols, rows)
 
theta = 0

while True:
    w_ = cols * abs(math.cos(math.radians(theta))) + rows * abs(math.sin(math.radians(theta)))
    h_ = cols * abs(math.sin(math.radians(theta))) + rows * abs(math.cos(math.radians(theta)))
   
   
    M = np.float32([[1,0,(w_/2 - cols/2)],[0,1,(h_/2 - rows/2)]])
    img_res = cv2.warpAffine(img_orig, M, (int(w_), int(h_)))
   
    cv2.imshow("",img_res)
    
    key = cv2.waitKey(0)

   
    if key == 27:   # ESC
        break

    if key == 32:   # Spacebar
        if theta == 360:
            break

        cv2.destroyAllWindows()
          
        theta += 10
        #print(theta)

        


cv2.destroyAllWindows()