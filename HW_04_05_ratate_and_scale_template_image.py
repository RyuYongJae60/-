import os
import cv2
import math

os.chdir(os.path.dirname(os.path.abspath(__file__)))

img_origin = cv2.imread("fish.png", 0)

scale = [0.5, 1.0, 1.5]
theta = 0
i=0
   
while True:
    img_resize = cv2.resize(img_origin, (0, 0), fx=scale[i], fy=scale[i])
    rows, cols = img_resize.shape   # rows: h, cols: w
    
    radian = math.radians(theta)
    w_ = cols*abs(math.cos(radian)) + rows*abs(math.sin(radian))
    h_ = cols*abs(math.sin(radian)) + rows*abs(math.cos(radian))

    M = cv2.getRotationMatrix2D((cols/2, rows/2), theta, 1) 
    M[0][2] = M[0][2] + (w_/2 - cols/2)
    M[1][2] = M[1][2] + (h_/2 - rows/2)

    print(str(scale[i]) + ', ' + str(theta))
    img_res = cv2.warpAffine(img_resize, M, (int(w_), int(h_)))
    cv2.imshow("", img_res)   
    key = cv2.waitKey(0)

    if key == 27:   # ESC
        break
    
    if key == 32:   # Spacebar
        theta += 10

        if theta == 360 and i == 2:
            break

        if theta == 360:
            i += 1
            theta = 0

        cv2.destroyAllWindows()

cv2.destroyAllWindows()