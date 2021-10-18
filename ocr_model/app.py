from flask import Flask, make_response, request
import numpy as np
import pandas as pd
import os
from PIL import Image
from create_csv.process_images import process_image
from create_model import create_model

app = Flask(__name__)

model = create_model('data.csv')

def get_predicted_value(model, data):
    return model.predict(data)

characters = {
    1.0: "අ",
    21.0: "ක",
    54.0: "ව",
    12.0: "ර"
}

@app.route("/")
def home():
    return make_response({
        "home": "Home"
    })

@app.route("/get_ocr", methods=['POST'])
def get_ocr():

    if(request.method=='POST'):
        if 'image' not in request.files:
            return 'not image in form'
        image = request.files['image']
        upload_image(image)
        #img = Image.open(image.filename)
        #img.show()
        arr = process_image('save/image.png')
        arr = arr.reshape(1,-1)
        print(arr)
        y_predict = get_predicted_value(model, arr)
        print(y_predict)
        print(characters[y_predict[0]])

    return make_response({
        "predicted_result": characters[y_predict[0]]
    })

def upload_image(image):
    path = os.path.join('save/image.png')
    image.save(path)

if __name__ == "__main__":
    app.debug(True)
    app.run(host='0.0.0.0')