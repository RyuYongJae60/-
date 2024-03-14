import os
import cv2

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image as grayscale
img_orig = cv2.imread('fish.png', 0)
rows,cols = img_orig.shape

theta = 0

while True:
    # Rotaion
    M = cv2.getRotationMatrix2D((cols/2,rows/2), theta, 1)
    img_res = cv2.warpAffine(img_orig, M, (cols,rows))
   
    cv2.imshow("",img_res)
    
    key = cv2.waitKey(0)
    

    if key == 27:   # ESC
        break

    
    if key == 32:   # Spacebar
        if theta == 360:
            break
 
        theta += 10
        #print(theta)


cv2.destroyAllWindows()