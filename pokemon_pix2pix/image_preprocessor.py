import numpy as np
import tensorflow as tf

def normalize(input_image):
    input_image = (input_image / 127.5) - 1

    return input_image

def denormalize(input_image):
    input_image = (input_image + 1) * 127.5
    input_image = input_image.numpy()

    return input_image.astype(np.uint8)

def load_image(image_file):
    image = tf.image.decode_jpeg(image_file)
    image = tf.cast(image, tf.float32)

    return image

def resize(input_image, height, width):
    input_image = tf.image.resize(input_image, [height, width], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)

    return input_image

def preprocess(src, width, height):
    input_image = load_image(src)
    input_image = resize(input_image, height, width)
    input_image = normalize(input_image)

    return input_image