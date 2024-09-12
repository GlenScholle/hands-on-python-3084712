import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
print(einstein_json)
pprint(back_to_dict)

with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


with open("laureates.json", "w", encoding="utf-8") as f2:
    json.dump(laureates, f2, indent=2)
