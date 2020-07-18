import io, os
from google.cloud import vision
import requests
from pprint import pprint

pload = {
 "appId" : "042872e7",
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
 "query" : "apple"
}


r = requests.post("https://api.nutritionix.com/v1_1/search", data = pload)
print(r.json)
item = r.json()["hits"][0]["fields"]
str = "Nome: " + item["item_name"] + "\n" \
    + "Calorie: " + str(item["nf_calories"]) + " kcal\n" \
    + "Colesterolo: " + str(item["nf_cholesterol"]) + " mg\n" \
    + "Sodio: " + str(item["nf_sodium"]) + " mg\n" \
    + "Vitamina C: " + str(item["nf_vitamin_c_dv"]) + "%"

print(str)


