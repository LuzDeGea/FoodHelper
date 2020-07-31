import requests
from Food import Food

def traduzione(msg):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = "source=it&q="+msg+"&target=en"
    headers = {
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "0e02a9f55dmsh53204c2910d6aeap14f2c6jsn2cac795c2119",
        'accept-encoding': "application/gzip",
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print("Traduzione: "+response.json()["data"]["translations"][0]["translatedText"])
    return response.text

def get_food(food):
    #File jason da inviare in POST
    pload = {
        "appId": "042872e7",
        "appKey": "50de4a27e46b09fa8b66f1b41cbfe8bf",
        "min_score": 2,  ##Test##
        "fields": [
            "item_name",  ##Test##
            "nf_calories",
            "nf_total_carbohydrate",
            "nf_cholesterol",
            "nf_iron_dv",
            "nf_total_fat",
            "nf_ingredient_statement",
            "nf_protein",
            "nf_sodium",
            "nf_sugars"
        ],
        "query": food
    }
    #Richiesta HTTP POST
    r = requests.post("https://api.nutritionix.com/v1_1/search", data = pload)
    print(r.json())
    if "error_message" in r.json().keys():
        return False
    elif r.json()["total"] == 0:
        return False
    else:
        return Food(food, r.json()["hits"][0]["fields"])
