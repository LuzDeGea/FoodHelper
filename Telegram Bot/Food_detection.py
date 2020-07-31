import io, os
from google.cloud import vision
from Nutrition import get_food

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"API_key\\Vision_key.json"
client = vision.ImageAnnotatorClient()

file_name = r"Immagini\\Cibo.png"

### Cose da scartare ###
scarti = {"Food","Meal","Cuisine","Dish","Ingredient","Vegetable","Bowl","Person",
          "Finger","Tableware","Brunch","Supper","Appetizer","Recipe","Lunch",
          "Produce","Finger food","Staple food","Whole food","Local food",
          "Food group","Italian food","Comfort food","Vegetarian food",
          "Vegan nutrition","American food","Platter","À la carte food",
          "Cooking","Banana family","Al dente","Cruciferous vegetables",
          "Fruit","Breakfast","Dessert","Baked goods","Sweetness",
          "Frozen dessert","Mirror","Natural foods","Whole food",
          "Meat","Fried food","Plant","Local food"}
tipo_no = {"Superfood","Junk food","Fast food"}

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
            if not(food.description in scarti):
                return food.description
        return False
    else:
        return False
