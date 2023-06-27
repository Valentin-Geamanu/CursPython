# INTERACTYIUNEA CU FISIERE JSON
"""
JSON = Javascript Object Notation


citire din fisier json:

metoda json.load()
-folosim aceasta metoda ca sa incarcam/decodam un obiect de tip json 
dintr-un fisier .

fisier json --> obiect corespunzator python

"""
import json


def citire_din_fisier_json(cale_fisier):
    with open(cale_fisier, 'r') as file:
        return json.load(file)


data = citire_din_fisier_json()
print(type(data))
sport_question = data['quiz']['sport']['q1']['question']
print(sport_question)
quiz = data['quiz']
sport_category = quiz['sport']
q1 = sport_category['q1']
question = q1






def scriere_in_fisier_json(cale_fisier, randuri_informatii):
    with open(cale_fisier, 'w') as file:
        json.dump(randuri_informatii, file)