import csv
import os
from process_images import process_image
import numpy as np

list_images = os.listdir('images/')

#print(list_images)

def save_in_csv(filename, image_data, name):
    np_array = np.insert(image_data, 0, name, axis=0)
    print(np_array)
    ex= np_array.tolist()
    #print(ex)
    with open(filename+'.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(ex)

for i in list_images:
    name = i[i.find("_")+1:i.find(".")]
    #print(float(name))
    img = process_image('images/'+i)
    #print(img)
    #print("float val : ",img," value: ",name)
    save_in_csv('data', img, name)



