import json

jdata = '{"marka":"Land Rover","model":"Defender","rocznik":2022,"poj":5.3}'

print(jdata)
print(type(jdata))

samochod = json.loads(jdata)
print(samochod)
print(type(samochod))
print(samochod["model"])

kolor = {
    "nazwa":"czarny",
    "id":5454,
    "paleta":"standard",
    "obraz":12,
    "znaki":"ąąąąćććńń"
}

jsonkolor = json.dumps(kolor,indent=4)
print(jsonkolor)

with open("kolory.json","w",encoding="utf-8") as f:
    f.write(jsonkolor)

print("_"*30)
with open("kolory.json","r",encoding="utf-8") as f:
    kolordict = json.load(f)

print(kolordict)
