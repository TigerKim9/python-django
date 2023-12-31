from django.apps import AppConfig
# from keras.models import load_model
from tensorflow.keras.models import load_model
import os

class AreyouidolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    name = 'AreYouIdol'
    model = load_model('model/model_vgg16_ver1.h5')
    img_path = os.path.join('media', 'images')
    crop_path = os.path.join('media', 'cropimages')
    print('경로이름 => ',crop_path)