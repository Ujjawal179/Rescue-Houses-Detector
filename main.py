import imagegenerator as img

image = (img.imagegen(r'round2/uas/images/image1.png'))
unburnt_red, unburnt_blue = img.get_info(image, (250,252,83))
burnt_red, burnt_blue = img.get_info(image, (134,251,252))
print(burnt_red, burnt_blue )
print(unburnt_red, unburnt_blue )
