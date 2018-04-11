import cv2
import numpy as np
#uncomment line under this and replace with image of your choosing
#img=cv2.imread("bob6.png",1)

    
def redcheck(img):
    red=img[:,:,2] 
    ret,thresh1 = cv2.threshold(red,100,255,cv2.THRESH_BINARY)
    (x,y)=(0,0)
    (x2,y2)=(0,0)
    
    kernel = np.ones((8,8),np.uint8)
    kernel2 = np.ones((5,5),np.uint8)
    thresh1 = cv2.erode(thresh1,kernel,iterations = 1)
    thresh1 = cv2.dilate(thresh1,kernel2,iterations = 1)
    thresh1 = cv2.morphologyEx(thresh1,cv2.MORPH_CLOSE,kernel)
    thresh1 = cv2.erode(thresh1,kernel2,iterations = 1)
    thresh1 = cv2.morphologyEx(thresh1,cv2.MORPH_CLOSE,kernel)
    
    
    _,cnts,_ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    xmax=[]
    xmaxr=[]
    for i in cnts:
         x=cv2.contourArea(i)
         if x>300:
             xmaxr.append(i)
             xmax.append(x)
    for i in xmaxr:
        rect = cv2.minAreaRect(i)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        print(box)
        cv2.drawContours(img,[box],0,(0,0,255),2)
    
    
    return xmaxr,thresh1

cont,img2=redcheck(img)
cv2.imshow("red",img)    
    
