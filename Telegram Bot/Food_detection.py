import io, os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"newagent-qwujpw-1825a9e19cd1.json"
client = vision.ImageAnnotatorClient()

file_name = "C:\\Users\\anton\\FoodHelper\\Telegram Bot\\Cibo.png"

def food_detection():
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    food_string = ""
    for food in response.label_annotations:
       food_string += "\n" + food.description
    return str(food_string)



