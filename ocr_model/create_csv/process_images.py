from PIL import Image
import numpy as np

def process_image(path):
    resize_image(path)
    image = Image.open(path)
    data = list(image.getdata())
    hex_val=rgb_to_hex(data,1)
    
    data_list =  []
    for i in range(len(data)):
        hex_val = rgb_to_hex(data, i)
        
        data_list.append(hex_to_float(hex_val))
    
    np_data_list = np.array(data_list)
    print(np_data_list)
    return np_data_list


def resize_image(path):
    image = Image.open(path)
    image = image.resize((64,64), Image.ANTIALIAS)
    image.save(path)
    



def rgb_to_hex(data, i):
    get_hex = '#{:02x}{:02x}{:02x}'.format(*data[i])
    return get_hex

def hex_to_float(hex_val):
    return float(int(str(hex_val)[1:], 16)/100000000)

process_image('images/අ1_1.pnglow.png')

# image = Image.open('create_csv/images/අ1_1.pnglow.png')

# image = image.resize((64,64), Image.ANTIALIAS)

# image.save('අ1_1.pnglow.png')
# image = Image.open('අ1_1.pnglow.png')

# print(image.mode)
# print(image.getpixel((10,20)))
# print(image.getdata())
# data = list(image.getdata())
# get_hex='#{:02x}{:02x}{:02x}'.format(*data[1])
# print(get_hex[1:])
# print(int(str(get_hex[1:]), 16))

# data_list = []

# for i in range(len(data)):
#     get_hex='#{:02x}{:02x}{:02x}'.format(*data[i])
#     #print(get_hex[1:])
#     #print(int(str(get_hex[1:]), 16))
#     data_list.append(
#         float(int(str(get_hex[1:]), 16)/100000000)
#     )

# print(data_list[5])