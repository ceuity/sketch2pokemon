from flask import Flask, render_template, request, Response, send_from_directory

import os

import tensorflow as tf
from PIL import Image
import numpy as np

from image_preprocessor import preprocess, denormalize
from pix2pix import load_pix2pix_model, generate_image

model = load_pix2pix_model()
app = Flask(__name__, template_folder="./templates/",
			static_url_path="/images", static_folder="images")

@app.route("/")
def index():
	return render_template('index.html')


@app.route("/healthz", methods=['GET'])
def healthCheck():
	return "", 200


@app.route("/images", methods=['POST'])
def get_result():
	if request.method == "POST":
		width, height = 256, 256
		try:
			source = request.files['source'].read()
			adjusted_image = preprocess(source, width, height)
			image = denormalize(adjusted_image)
			result = generate_image(model, adjusted_image)
			image = Image.fromarray(result)
			image_path = './images/'
			filename = 'result_image.png'
			image.save(image_path + filename)
			
			return send_from_directory(image_path, filename, as_attachment=True)

		except Exception as e:
			print("error : %s" % e)
			return Response("fail", status=400)

		
if __name__ == '__main__':
	app.run(host='0.0.0.0', port='80')
