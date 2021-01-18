import numpy as np
import cv2

def findC(masks):

    for m in masks:
        contours, hierarchy = cv2.findContours(m, 
                                                   cv2.RETR_TREE, 
                                                   cv2.CHAIN_APPROX_SIMPLE) 
                  
        for pic, contour in enumerate(contours): 
                x, y, w, h = cv2.boundingRect(contour) 
                imageFrame = cv2.rectangle(img,(x, y), (x + w, y + h),(0, 255, 0), 2)
            
    cv2.imshow("Red & green color detection: ", imageFrame)

img = cv2.imread("Colors.jpg", cv2.IMREAD_COLOR)
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Range for lower range
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
mask1 = cv2.inRange(hsvImg, lower_red, upper_red)

# Range for upper range
lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsvImg,lower_red,upper_red)

red_mask = mask1 + mask2

green_lower = np.array([25, 52, 72], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8) 
green_mask = cv2.inRange(hsvImg, green_lower, green_upper) 

findC([green_mask, red_mask])


key = cv2.waitKey(1)
if key == 27:
    cv2.destroyAllWindows()
