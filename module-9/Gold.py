#Dario Gomez assignment 9.2 4/24/2025
#program to show gold price.
import requests, json

response = requests.get("https://api.gold-api.com/price/XAU")
print(response.status_code)
print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())