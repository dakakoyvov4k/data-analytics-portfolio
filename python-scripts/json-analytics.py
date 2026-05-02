import json

d = {}

with open(r'manager_sales.json') as file:
    for k in json.load(file):
        d[k['manager']['first_name'] + ' ' + k['manager']
        ['last_name']] = sum([i['price'] for i in k['cars']])

print(*sorted(d.items()))

dd = {}

with open(r'group_people.json') as file:
    for item in json.load(file):
        count = 0
        for female in item['people']:
            if female['gender'] == 'Female' and female['year'] > 1977:
                count += 1
        dd[item['id_group']] = count
print(*sorted(dd.items())) #в 9 группе 10 женщин
