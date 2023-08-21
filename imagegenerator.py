import cv2
import numpy as np

def imagegen(path):
    '''
    Function returns a image
    distinguishing between the burnt and unburnt grass
    without changing the positions of the triangle
    '''
    # loading the image using path input
    image = cv2.imread(path)
    
    # converting the image to hsv for analysis
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # creating a mask for green grass
    mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

    # making a np array of image size having zeros in unit8 data type
    # Uint8's are mostly used in graphics 
    result  = np.zeros_like(image, np.uint8)
    
    # using the mask 
    imask = mask<1
    result[imask] = [134,251,252]
    imask = mask>0
    result[imask] = [250,252,83]

    # Creating masks for triangles and setting them to respective colors
    mask= cv2.inRange(hsv, (90, 50, 70),(128, 255, 255))
    imask = mask>0
    result[imask] = [240,18,0]
    mask= cv2.inRange(hsv, (0, 50, 70),(9, 255, 255))
    imask = mask>0
    result[imask] = [43,10,255]

    # Returning the image
    return result



def display(result):
    '''
    This funtion shows the image
    (Used while testing of program)
    '''

    cv2.imshow('Image',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def get_info(result, rgb):
    '''
    get_info returns the numbers of 
    red and blue houses which lies in 
    range of given color area

    it takes the image for imagegen funtion
    for the best precision
    '''

    # variable for storing Number of houses 
    blue  , red = 0,0

    # taking the image and color for creating a mask 
    img = cv2.inRange(result,rgb,rgb)
    
    # Taking a matrix of size 4 as the kernel
    kernel = np.ones((4, 4), np.uint8)

    # The first parameter is the original image,
    # kernel is the matrix with which image is
    # convolved and third parameter is the number
    # of iterations, which will determine how much
    # you want to erode/dilate a given image.
    dilation = cv2.dilate(img, kernel, iterations=1)

    # applying gaussian blur and threshold to image
    # for better identification of the shapes
    img = cv2.GaussianBlur(dilation, (5, 5), 0)
    _, img = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY_INV)

    # getting the corners
    contours,hierarchy = cv2.findContours(img, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # filling the unnecessary gaps of 5 pixcel thickness
    for cnt in contours:
        img = cv2.drawContours(img,[cnt],0,255,5)

    # getting the corners
    contours,hierarchy = cv2.findContours(img, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    # getting the approx shape
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.1*cv2.arcLength(cnt, True), True)

        # checking if the shape is triangle or not
        if len(approx) == 3:

            # compute the center of mass of the triangle
            M = cv2.moments(cnt)

            if M['m00'] != 0.0:
                # Getting the co-ordinates of the centroid of the triangle
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])
                
                # checking the color of centroid and adding values of houses 
                # if condition is satisfied
                if any(result[y,x] == (240,18,0)):
                    blue+=1
                elif any(result[y,x] == [43,10,255]):
                    red+=1
    # returning the values of number of houses
    return red, blue




# Here are some color references 

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
