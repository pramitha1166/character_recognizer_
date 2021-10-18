from PIL import Image

image = Image.open('create_csv/images/අ1_1.pnglow.png')

image = image.resize((64,64), Image.ANTIALIAS)

image.save('අ1_1.pnglow.png')
image = Image.open('අ1_1.pnglow.png')

print(image.mode)
print(image.getpixel((10,20)))
print(image.getdata())
data = list(image.getdata())
get_hex='#{:02x}{:02x}{:02x}'.format(*data[1])
print(get_hex[1:])
print(int(str(get_hex[1:]), 16))

data_list = []

for i in range(len(data)):
    get_hex='#{:02x}{:02x}{:02x}'.format(*data[i])
    #print(get_hex[1:])
    #print(int(str(get_hex[1:]), 16))
    data_list.append(
        float(int(str(get_hex[1:]), 16)/100000000)
    )

print(data_list[5])