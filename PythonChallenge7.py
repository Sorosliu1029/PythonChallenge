"""
this challenge is not hard, but quite time-consuming
keep patient, and you will find the rules in the image
focused on the blur area
"""
from PIL import Image


def get_vertical_area(img):
    vertical_pixels = [img.getpixel((0, i)) for i in range(img.size[1])]
    vertical_blur_area = [i for i in range(img.size[1]) if vertical_pixels[i][0] == vertical_pixels[i][1] and
                          vertical_pixels[i][1] == vertical_pixels[i][2]]
    return vertical_blur_area[0], vertical_blur_area[-1]


def get_horizontal_area(img):
    horizontal_pixels = [img.getpixel((i, 43)) for i in range(img.size[0])]
    horizontal_blur_area = [i for i in range(img.size[0]) if horizontal_pixels[i][0] == horizontal_pixels[i][1] and
                            horizontal_pixels[i][1] == horizontal_pixels[i][2]]
    return horizontal_blur_area[0], horizontal_blur_area[-1]

img = Image.open('oxygen.png')
print(img.size)
vertical_range = get_vertical_area(img)
horizontal_range = get_horizontal_area(img)
print(vertical_range, horizontal_range)
print([img.getpixel((i, 43)) for i in range(20)])
# From above methods, we will find some rules in this image
# In the blur area, it ranges from 43~51 vertically, 0~607 horizontally, with a 7 step length
data = [img.getpixel((i, 43))[0] for i in range(0, 607, 7)]
print(data)
secret = ''.join(list(map(chr, data)))
print(secret)
# above method give the information '[105, 110, 116, 101, 103, 114, 105, 116, 121]'
char_list = []
exec('char_list = ' + secret[secret.find('['):])
print(''.join((list(map(chr, char_list)))))
# Finally..... :~)
