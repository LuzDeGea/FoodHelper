import os, io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'foodhelper-sysag-356f63fafc5e.json'

client = vision.ImageAnnotatorClient()
