import csv
import os
from process_images import process_image

list_images = os.listdir('images/')

#print(list_images)

for i in list_images:
    name = i[i.find("_")+1:i.find(".")]
    print(float(name))
    
