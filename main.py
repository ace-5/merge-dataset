import enchant
import json

from rx import merge
district_list = enchant.PyPWL('districts_of_Nepal.txt')

data = [{'Kathmandu':0.8, 'Dhanusa':0.85, 'Kavre palanchowk':0.75},
    {'Kathmandu':0.35, 'Kavrepalanchowk':0.65, 'Dhanusha':0.6}]

merged = {}
for items in data:
    for k,v in items.items():
        k = district_list.suggest(k)[0]
        if k in merged.keys():
            merged[k].append(v)
        else:
            merged[k] = [v]

with open('output.json', 'w') as f:
    f.write(json.dumps(merged))