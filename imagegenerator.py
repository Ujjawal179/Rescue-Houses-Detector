import cv2
import numpy as np

def imagegen(path):
    image = cv2.imread(r'F:\coding\round2\uas\images\image1.png')  # path will bw addded later
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

    result  = np.zeros_like(image, np.uint8)

    imask = mask<1
    result[imask] = [134,251,252]
    imask = mask>0
    result[imask] = [250,252,83]

    mask= cv2.inRange(hsv, (90, 50, 70),(128, 255, 255))
    imask = mask>0
    result[imask] = [240,18,0]
    mask= cv2.inRange(hsv, (0, 50, 70),(9, 255, 255))
    imask = mask>0
    result[imask] = [43,10,255]
    return result
    
def display(result):
    cv2.imshow('Image',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_info(result, rgb):
    blue  , red = 0,0
    img = cv2.inRange(result,rgb,rgb)

    kernel = np.ones((4, 4), np.uint8)
    dilation = cv2.dilate(img, kernel, iterations=1)

    img = cv2.GaussianBlur(dilation, (5, 5), 0)
    _, img = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY_INV)

    contours,hierarchy = cv2.findContours(img, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        img = cv2.drawContours(img,[cnt],0,255,5)
    contours,hierarchy = cv2.findContours(img, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.1*cv2.arcLength(cnt, True), True)
        if len(approx) == 3:

            # compute the center of mass of the triangle
            M = cv2.moments(cnt)
            if M['m00'] != 0.0:
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])
                
                if any(result[y,x] == (240,18,0)):
                    blue+=1
                elif any(result[y,x] == [43,10,255]):
                    red+=1

    return red, blue






# cyan  134,251,252
# yell 250,252,83
# Red 240,18,0
# Blue 43,10,255

'''

color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}
'''
