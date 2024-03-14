import os
import cv2
import numpy as np
import math

os.chdir(os.path.dirname(os.path.abspath(__file__)))

img_origin = cv2.imread("fish.png", 0)
reference = ["test_1.png", "test_2.png", "test_3.png"]
idx=0

scale = [0.5, 1.0, 1.5]
i=0
theta = 0


while True:
    ref_img = cv2.imread(reference[idx], 0)
    
    s = scale[i]   
    img_resize = cv2.resize(img_origin, (0, 0), fx=s, fy=s)
    rows, cols  = img_resize.shape  # rows: h, cols:w


    radian = math.radians(theta)
    w_ = cols * abs(math.cos(radian)) + rows * abs(math.sin(radian))
    h_ = cols * abs(math.sin(radian)) + rows * abs(math.cos(radian))



    M = cv2.getRotationMatrix2D((cols/2, rows/2), theta, 1)
    M[0, 2] += (w_/2 - cols/2)
    M[1, 2] += (h_/2 - rows/2)

    img_res = cv2.warpAffine(img_resize, M, (int(w_), int(h_)))
    res_h, res_w = img_res.shape

    mask = np.zeros((rows, cols), np.uint8)
    mask[1:-1, 1:-1] = 255
    img_mask = cv2.warpAffine(mask, M, (int(w_), int(h_)))
    #print(mask)
    cv2.imshow("mask", img_mask)
    cv2.imshow("resImage", img_res)
    
    img_matching_scores = cv2.matchTemplate(ref_img, img_res, cv2.TM_CCORR_NORMED, mask = img_mask)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_matching_scores)
    #cv2.imshow("", img_matching_scores)

    top_left = max_loc
    bottom_right = (top_left[0] + res_w, top_left[1] + res_h)
    
    img_found = cv2.cvtColor(ref_img, cv2.COLOR_GRAY2BGR)

    cv2.rectangle(img_found, top_left, bottom_right, [0, 0, 255], 2)
    cv2.imshow("A", img_found)
    
    key = cv2.waitKey(0)


    if key == 27:   # ESC
        break

    # 스페이스바 한번 누르면 test_1 -> test_2 -> test_3 순으로 표시.
    if key == 32:   # Spacebar
        theta += 10
        if i==2 and theta == 360:
            cv2.destroyAllWindows()
            idx += 1
            i = 0
            theta = 0

        if idx == 3:
            break      

        if theta == 360:
            theta = 0
            i += 1
            
 
cv2.destroyAllWindows()