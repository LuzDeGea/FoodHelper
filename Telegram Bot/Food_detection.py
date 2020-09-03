import io, os
from google.cloud import vision
from Nutrition import get_food
import csv

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"API_key\\Vision_key.json"
client = vision.ImageAnnotatorClient()

file_name = r"Immagini\\Cibo.png"

### Cose da scartare ###
tipo_no = {"Superfood","Junk food","Fast food"}

filtro=[]
filter_name = "filtro_s.csv"
with open(filter_name, 'r') as csv_filter:
    csv_filter = csv.reader(csv_filter)
    for row in csv_filter:
        filtro.append(row[0])
#print (filtro)

def food_detection():
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)

    cibo_p = filtering(response)
    if cibo_p:
        return get_food(cibo_p)
    else:
        return False

def ConteinsLabel(response, in_lable):
    for food in response.label_annotations:
        if food.description == in_lable:
           return True
    return False

def filtering(response):
    if ConteinsLabel(response,"Food") or ConteinsLabel(response,"Plant"):
        for food in response.label_annotations:
            if not(food.description in filtro):
                return food.description
        return False
    else:
        return False
