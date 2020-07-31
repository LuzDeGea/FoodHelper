import requests
from Food import Food

def get_food(food):
    #File jason da inviare in POST
    pload = {
        "appId": "042872e7",
        "appKey": "50de4a27e46b09fa8b66f1b41cbfe8bf",
        "fields": [
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
    if r.json()["total"] == 0:
        return False
    else:
        return Food(food, r.json()["hits"][0]["fields"])
