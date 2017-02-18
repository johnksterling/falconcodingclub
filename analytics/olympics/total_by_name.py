import csv
import datetime


year_list = []
count_list = []

YEAR_INDEX = 0
NAME_INDEX = 4
COUNTRY_INDEX = 5
MF_INDEX = 6
CATEGORY_INDEX = 2
EVENT_INDEX = 3
names = {}
with open('summer.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        name = row[NAME_INDEX]
        if not names.get(name):
            names[name] = 0
        names[name] += 1

name_list = sorted(names, key=names.get)
bottom5 = name_list[0:10]
top5 = name_list[-20:]
for name in top5:
    print(name + ': ' + str(names[name]))
