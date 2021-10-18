from flask import Flask, make_response, request
import numpy as np
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('new_data.csv')


@app.route("/")
def home():
    return make_response({
        "home": "Home"
    })

@app.route("/get_ocr")
def get_ocr():
    return make_response({
        "predicted_result": "preadicted abc"
    })

if __name__ == "__main__":
    app.debug(True)
    app.run(host='0.0.0.0')