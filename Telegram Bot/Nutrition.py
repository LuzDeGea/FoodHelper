import requests

def get_valori(food):
    #File jason da inviare in POST
    pload = {
        "appId": "042872e7",
        "appKey": "50de4a27e46b09fa8b66f1b41cbfe8bf",
        "fields": [
            "item_name",
            "brand_name",
            "nf_calories",
            "nf_sodium",
            "nf_cholesterol",
            "nf_vitamin_c_dv",
            "item_type"
        ],
        "query": food
    }
    #Richiesta HTTP POST
    r = requests.post("https://api.nutritionix.com/v1_1/search", data = pload)

    #Risultato
    item = r.json()["hits"][0]["fields"]
    value = "Nome: " + food + "\n" \
        + "Calorie: " + str(item["nf_calories"]) + " kcal\n" \
        + "Colesterolo: " + str(item["nf_cholesterol"]) + " mg\n" \
        + "Sodio: " + str(item["nf_sodium"]) + " mg\n" \
        + "Vitamina C: " + str(item["nf_vitamin_c_dv"]) + "%"

    return value
