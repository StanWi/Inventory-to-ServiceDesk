import csv

'''
Structure:
{CTE: {
       Location: {
                  Category: {
                             ShelfType: {
                                         [Slot, Module, Vendor, Serial]}}}}}
'''
locations_file = 'locations.csv'
items_file = 'in_work.csv'

locations = {}
items = []

base = {'Оптика': [],
        'WDM': ['XDM-1000', 'XDM-500', 'XDM-40'],
        'SDH': ['AXX 9300 METRO', 'OMS-870', 'OMS-860'],
        'PDH': ['Транспорт-30x4'],
        'Приборы': ['Exfo'],
        'Климат': [],
        'Серверы и ПО': [],
        'Оптические модули': ['SFP', 'XFP']}

with open(locations_file, encoding='utf-8') as csvfile:
    loc_reader = csv.reader(csvfile)
    loc_reader.__next__() # Skip header
    for row in loc_reader:
        locations.setdefault(row[1], [])
        locations[row[1]].append(row[0])

# print(locations)

with open(items_file, encoding='cp1251') as csvfile:
    item_reader = csv.reader(csvfile, delimiter=';')
    item_reader.__next__()
    for row in item_reader:
        items.append(row)

for i in range(5):
    print(items[i])

