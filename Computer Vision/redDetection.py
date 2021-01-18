import numpy as np
import cv2

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

maskF = mask1 + mask2
contours, hierarchy = cv2.findContours(maskF, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
          
for pic, contour in enumerate(contours): 
        x, y, w, h = cv2.boundingRect(contour) 
        imageFrame = cv2.rectangle(img,(x, y), (x + w, y + h),(0, 255, 0), 2)
        
cv2.imshow("Red color detection", imageFrame)
cv2.imshow("Red color detection 2", red)

key = cv2.waitKey(1)
if key == 27:
    cv2.destroyAllWindows()
