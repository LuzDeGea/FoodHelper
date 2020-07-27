import io, os
from google.cloud import vision
from Nutrition import get_valori

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"API_key\\Vision_key.json"
client = vision.ImageAnnotatorClient()

file_name = r"Immagini\\Cibo.png"

### Cose da scartare ###
scarti = {"Food","Meal","Cuisine","Dish","Ingredient","Vegetable","Bowl","Person",
          "Finger","Tableware","Brunch","Supper","Appetizer","Recipe","Lunch",
          "Produce","Finger Food","Staple Food","Whole Food","Local Food",
          "Food Group","Italian Food","Comfort Food","Vegetarian Food",
          "Vegan Nutrition","American Food","Platter","À La Carte Food",
          "Cooking","Banana family","Al dente","Cruciferous vegetables",
          "Fruit","Breakfast","Dessert","Baked goods","Sweetness",
          "Frozen Dessert","Mirror","Natural foods","Whole food",
          "Meat","Fried food","Plant","Local food"}
tipo_no = {"Superfood","Junk Food","Fast Food"}

def food_detection():
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)

    #for food in response.label_annotations:
    #   print(food.description)

    cibo_p = filtering(response)
    print(cibo_p)
    if cibo_p:
        return "Il cibo riconosciuto dovrebbe essere: " + cibo_p + "\n" + get_valori(cibo_p)
    else:
        return "Cibo non riconosciuto correttamente"

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
