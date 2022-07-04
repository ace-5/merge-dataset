import enchant
import csv
district_list = enchant.PyPWL('districts_of_Nepal.txt')

data = [{'Kathmandu':0.8, 'Dhanusa':0.85, 'Kavre palanchowk':0.75},
    {'Kathmandu':0.35, 'Kavrepalanchowk':0.65, 'Dhanusha':0.6}]

merged = {
    'District': []
}
for i in range(len(data)):
    merged[f'KPI_{i+1}'] = []
    for k,v in data[i].items():
        k = district_list.suggest(k)[0]
        if k not in merged['District']:
            merged['District'].append(k)
        merged[f'KPI_{i+1}'].append(v)

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(merged.keys())
    writer.writerows(zip(*merged.values()))