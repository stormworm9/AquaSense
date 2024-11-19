import io
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Conv2D, BatchNormalization, ReLU, Conv2DTranspose

IMG_SIZE = 256

class ConvBlock(tf.keras.layers.Layer):
    def __init__(self, filters=512, kernel_size=3, dilation_rate=1, **kwargs):
        super(ConvBlock, self).__init__(**kwargs)
        self.filters = filters
        self.kernel_size = kernel_size
        self.dilation_rate = dilation_rate
        self.net = Sequential([
            Conv2D(filters, kernel_size, padding='same', dilation_rate=dilation_rate, activation=None, use_bias=False),
            BatchNormalization(),
            ReLU()
        ])

    def call(self, inputs):
        return self.net(inputs)

    def get_config(self):
        config = super().get_config()
        config.update({
            'filters': self.filters,
            'kernel_size': self.kernel_size,
            'dilation_rate': self.dilation_rate
        })
        return config

def load_keras_model(model_name):
    custom_objects = {"ConvBlock": ConvBlock}
    try:
        if model_name == "U-Net":
            return load_model('./Model/unet.keras', compile=False)
        else:  # DeepLabV3+
            return load_model('./Model/deeplabv3+.h5', custom_objects=custom_objects, compile=False)
    except Exception as e:
        raise RuntimeError(f"Error loading model: {str(e)}")

def preprocess_image(image):
    img_array = np.array(image)
    original_size = img_array.shape[:2]
    img_resized = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    img_normalized = img_resized / 255.0
    img_batch = np.expand_dims(img_normalized, axis=0)
    return img_batch, original_size

def postprocess_prediction(prediction, original_size):
    threshold = 0.5
    binary_mask = (prediction > threshold).astype(np.uint8)
    binary_mask = np.squeeze(binary_mask)
    mask_resized = cv2.resize(binary_mask, (original_size[1], original_size[0]))
    mask_image = Image.fromarray(mask_resized * 255)
    return mask_image

def create_overlay(original_image, mask_image, opacity=0.3):
    original_array = np.array(original_image)
    mask_array = np.array(mask_image)
    overlay = original_array.copy()
    water_mask = mask_array > 0
    overlay[water_mask] = [65, 105, 225]  # Royal Blue color for water
    blended = cv2.addWeighted(original_array, 1-opacity, overlay, opacity, 0)
    return Image.fromarray(blended)

def create_mask_visualization(mask_image):
    mask_array = np.array(mask_image)
    colored_mask = np.zeros((*mask_array.shape, 3), dtype=np.uint8)
    colored_mask[mask_array > 0] = [65, 105, 225]  # Royal Blue for water
    return Image.fromarray(colored_mask)