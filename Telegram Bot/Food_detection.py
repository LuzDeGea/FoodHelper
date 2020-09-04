import io, os
from google.cloud import vision
from Nutrition import get_food
import csv
import re

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"API_key\\Vision_key.json"
client = vision.ImageAnnotatorClient()

file_name = r"Immagini\\Cibo.png"

### Cose da scartare come sottostringa###
no_food = ["Food","Framily","Group","Superfood","Junk","Fast"]

"""
crea la lista da file, dei termini da scartare per la food_filter.
"""
filtro=[]
filter_name = "filtro_s.csv"
with open(filter_name, 'r') as csv_filter:
    csv_filter = csv.reader(csv_filter)
    for row in csv_filter:
        filtro.append(row[0])
#print (filtro)

"""
food_detection()-->string
prende dall'utente un'immagine o un testo e restituisce il
tipo più preciso, dato per il cibo.
"""
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

"""
ConteinsLabel(food_list,etichetta)-->bool
Restituisce vero nel caso in cui l'etichetta è presente nella food_list,
falso altrimenti.
"""
def ConteinsLabel(response, in_lable):
    for food in response.label_annotations:
        if food.description == in_lable:
           return True
    return False

"""
filtering(food_list)-->food
prende la lista predetta per il cibo ed elimina dall'alto le stringhe che 
risultano non di cibo (appartenenti a filtro) e quelle generiche 
(appartenenti a no_food), in caso non sia cibo, restituisce false.
"""
def filtering(response):
    if ConteinsLabel(response,"Food") or ConteinsLabel(response,"Plant"):
        for food in response.label_annotations:
            if not((food.description in filtro) and (contiene(food.description))):
                return food.description
        return False
    else:
        return False

"""
contiene(string)-->bool
definisce se è presente una etichetta come sotto-stringa nel nome del cibo
"""
def contiene(Etichetta):
    for food in no_food:
        if re.search(food.lower(),Etichetta.lower()):
            return False
    return True
