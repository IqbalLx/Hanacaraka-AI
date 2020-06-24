# Flask untuk web interface
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect

# TensorFlow dan tf.keras untuk AI
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image

# Numpy untuk pemrosesan matriks
import numpy as np

# utility
import re
import base64
import os
import sys

# inisialisasi Flask app
app = Flask(__name__)

# Tentukan path weight dan model yang sudah ditrain
MODEL_PATH = 'model/improved_model_v3.h5'

# Load model
model = load_model(MODEL_PATH)
#model._make_predict_function()     
    
# Msg ke server, model berhasil di-load
print('Model loaded. Start serving...')

value = ['ba', 'ca', 'da', 'dha', 'ga', 'ha', 'ja', 'ka', 'la', 'ma',
        'na', 'nga', 'nya', 'pa', 'ra', 'sa', 'ta', 'tha', 'wa', 'ya']

expected = ['ha', 'na', 'ca', 'ra', 'ka']

n_size = 100

# decoding image dari base64 ke representasi png
def convertImage(imgData1, play=False):
	if play:
		imgstr = re.search(b'base64,(.*)',imgData1).group(1)
	else:
		imgstr = re.search('base64,(.*)',imgData1).group(1)

	with open('image/output.png','wb') as output:
		output.write(base64.b64decode(imgstr))

# resize png dan convert ke grayscale
def normalized():
	x = keras_image.load_img("image/output.png",
							color_mode='grayscale',
							target_size=(n_size, n_size))
	x = keras_image.img_to_array(x)
	x = x - (x/255)

	# reshape image ke dimensi yang dibutuhkan model
	x = np.expand_dims(x, axis=0)
	x = np.vstack([x])
	print ("data prep stage")
	return x

@app.route('/')
def index():
	#initModel()
	# render out pre-built HTML file di halaman index
	return render_template("index.html")

@app.route('/predict/',methods=['GET','POST'])
def predict():
	# saat method dipanggil, angka yang digambar user akan dikonversi ke image. lakukan inference dengan model. kembalikan hasil klasifikasi
	# ambil raw data
	
	index = request.json['counter']
	imgData = request.json["img"]

	# encode ke image format
	convertImage(imgData)

	#normalized
	x = normalized()

	# prediksi
	out = model.predict(x)
	script = value[np.argmax(out)]
	expect = expected[int(index)]
	print(f'predicted: {script}, expected: {expect}')
	if script == expect:
		response = "1"
	else:
		response = "0"
	return response

@app.route('/predict_play/',methods=['GET','POST'])
def predict_play():
	# saat method dipanggil, angka yang digambar user akan dikonversi ke image. lakukan inference dengan model. kembalikan hasil klasifikasi
	# ambil raw data
	imgData = request.get_data()
	print('imgData :- ',type(imgData))

	# encode ke image format
	convertImage(imgData, play=True)

	#normalized
	x = normalized()

	# prediksi
	out = model.predict(x)
	response = value[np.argmax(out)]	
	return response
	
if __name__ == "__main__":
	# tentukan port mana app akan berjalan
	#port = int(os.environ.get('PORT', 5000))
	# locally run app
	#app.run(host='0.0.0.0', port=port)
	# optional if we want to run in debugging mode
	app.run()