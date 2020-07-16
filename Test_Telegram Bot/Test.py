import io, os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"newagent-qwujpw-1825a9e19cd1.json"
client = vision.ImageAnnotatorClient()

os.chdir("C:\\Users\\anton\\FoodHelper\\Test_Telegram Bot\\FileSysag")
file_name = "C:\\Users\\anton\\FoodHelper\\Test_Telegram Bot\\FileSysag\\Banane.jpg"
#image_path = os.join('.\lib\FileSysag', file_name)


with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.label_detection(image=image)
print(response)
