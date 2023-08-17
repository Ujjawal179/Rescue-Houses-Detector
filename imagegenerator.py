import cv2
import numpy as np

def imagegen(path):
    image = cv2.imread(r'F:\coding\round2\uas\images\image1.png')
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
    
    
    cv2.imshow('Image',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



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