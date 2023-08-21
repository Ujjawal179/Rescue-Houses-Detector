# Rescue-Houses-Detector

There's no doubt that technology is developing and causing many problems for us. For example, global warming results in grasslands and houses catching fire. Our solution to this problem is to make a Rescue house detector program that will detect the burnt grass, unburnt grass, and houses in them for Unmanned Aerial Vehicles (UAVs) to be able to rescue these persons according to their priorities. 

# Working
It takes images of grassland having houses shown as triangles on that image from images folder.

Functions:

imagegen --> distinguishing between the burnt and unburnt grass without changing the positions of the triangle

display --> This function shows the image, it is mostly used while testing of program

get_info --> It returns the numbers of  red and blue houses which lie in the range of given color area. It takes the image for imagegen function for the best precision

Outputs are stored in the output folder and lists are shown in Terminal.
