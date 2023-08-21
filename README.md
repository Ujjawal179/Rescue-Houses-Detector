# Rescue-Houses-Detector

There's no doubt that technology is developing and causing many problems for us. For example, global warming results in grasslands and houses catching fire. Our solution to this problem is to make a Rescue house detector program that will detect the burnt grass, unburnt grass, and houses in them for Unmanned Aerial Vehicles (UAVs) to be able to rescue these persons according to their priorities. 

# Working
It takes images of grassland having houses shown as triangles on that image from images folder.

Functions:

imagegen --> distinguishing between the burnt and unburnt grass without changing the positions of the triangle

display --> This function shows the image, it is mostly used while testing of program

get_info --> It returns the numbers of  red and blue houses which lie in the range of given color area. It takes the image for imagegen function for the best precision

Outputs are stored in the output folder and lists are shown in Terminal. Here is all the details:

1. An output image, for each input image, that clearly shows the difference between the
burnt grass and green grass, by overlaying 2 unique colors on top of each. The expected
output for the given sample input is given below
2. The number of houses on the burnt grass (Hb) and the number of houses on the green
grass (Hg), saved in a list
3. The total priority of houses on the burnt grass (Pb) and the total priority of houses on the
green grass (Pg), saved in a list
4. A rescue ratio of priority Pr where Pr = Pb
/ Pg
, saved in a list
5. A list of the names of the input images , arranges in descending order of their rescue ratio
(Pr)
