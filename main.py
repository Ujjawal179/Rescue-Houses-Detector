import imagegenerator as img
import cv2

n_houses = []
priority_houses = []
priority_ratio  = {}

n = 10   # n is the number of images saved in i.png format where i is interger

for i in range(n):    # here goes the main loop
    image = (img.imagegen(f'images/{i+1}.png'))    # loading the image

    # using get_info function from other file
    unburnt_red, unburnt_blue = img.get_info(image, (250,252,83))  
    burnt_red, burnt_blue = img.get_info(image, (134,251,252))

    # making the list/dic for main iutput 
    n_houses.append([burnt_red + burnt_blue, unburnt_red + unburnt_blue])
    priority_houses.append([burnt_red + burnt_blue*2, unburnt_red + unburnt_blue*2])
    priority_ratio[f'Image{i+1}'] = round((burnt_red + burnt_blue*2)/(unburnt_red + unburnt_blue*2),3)

    # storing the output image in output directory
    cv2.imwrite(f'output/Image{i+1}.png', image)

# giving main outputs
print('n_houses = ', n_houses)
print('priority_houses = ', priority_houses)
print('priority_ratio = ' , list(priority_ratio.values()))

# sorting the directory according to priority
values = sorted(list(priority_ratio.values()))
sorted_dict = {k: v for k, v in sorted(priority_ratio.items(), key=lambda item: item[1])}
print('image_by_rescue _ratio = ', list(reversed(sorted_dict.keys())))
