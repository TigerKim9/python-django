# from django.test import TestCase
from pathlib import Path
import os

crop_path = os.path.join('media', 'cropimages')
print(crop_path)

print(os.path.abspath(crop_path))
path = os.path.abspath('')
print(path)

ssss = Path(__file__).resolve().parent

print(ssss)
