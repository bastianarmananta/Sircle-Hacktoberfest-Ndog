import tensorflow as tf
from io import BytesIO
from PIL import Image
from fastapi import File, UploadFile
import numpy as np

def read_file(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

def predict_image(image, model_path='../model/model.h5'):
    model = tf.keras.models.load_model(model_path)
    image = np.asarray(image.resize((224, 224)))[..., :3]
    image = tf.keras.applications.mobilenet.preprocess_input(image)
    image = tf.expand_dims(image, 0)
    image = image/255.0
    prediction = model.predict(image)
    return 'fertil' if prediction[0][0] > 0.5 else 'infertil'

