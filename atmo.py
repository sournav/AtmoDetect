import cv2
import numpy as np
import math
#uncomment line under this and replace with image of your choosing
#img=cv2.imread("bob2.png",1)

#rotates image given angle
def rotateimg(img,angle):
    #allows both single channel, and multi channel images
    try:
        x,y=img.shape
    except:
        x,y,_=img.shape
    #rotation takes place
    M=cv2.getRotationMatrix2D((x/2,y/2),angle,1)
    img2=cv2.warpAffine(img,M,(x,y))
    return img2
#highlights and extracts red parts of image
def redcheck(img):
    #seperating the red channel
    red=img[:,:,2]
    #first thresholding
    ret,thresh1 = cv2.threshold(red,100,255,cv2.THRESH_BINARY)
    (x,y)=(0,0)
    (x2,y2)=(0,0)
    #initializing kernels for morph ops
    kernel = np.ones((8,8),np.uint8)
    kernel2 = np.ones((5,5),np.uint8)
    #morph ops
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
        #box coordinates
        print(box)
        #angle
        print(rect[2])
        cv2.drawContours(img,[box],0,(0,0,255),2)
        
        
    
    return xmaxr,thresh1

#test code
cont,img2=redcheck(img)
cv2.imshow("red",img)   
cv2.imshow("boi",img2)    
