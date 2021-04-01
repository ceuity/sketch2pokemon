import tensorflow as tf
from image_preprocessor import denormalize

def load_pix2pix_model():
	generator = tf.keras.models.load_model('/app/model/pix2pix_model.h5')

	return generator

def generate_image(model, sketch):
	pred = model(sketch[tf.newaxis,...], training=True)
	
	return denormalize(pred[0])
