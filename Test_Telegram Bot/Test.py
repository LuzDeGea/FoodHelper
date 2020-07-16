import os, io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'foodhelper-agent-okksgq-86b565602ff9.json'

client = vision.ImageAnnotatorClient()
