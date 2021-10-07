import tensorflow as tf
from fastapi import File, UploadFile


def read_file(file):
    return tf.keras.preprocessing.image.load_img(file, target_size=(224, 224))

def predict_image(image, model_path='../../model/model.h5'):
    model = tf.keras.models.load_model(model_path)
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet.preprocess_input(image)
    image = tf.expand_dims(image, 0)
    image = image/255.0
    prediction = model.predict(image)
    return 'fertil' if prediction < 0.5 else 'infertil'

