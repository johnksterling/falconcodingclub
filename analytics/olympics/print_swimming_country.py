import csv
import datetime


name = input('What country are you interested in (e.g. USA)? ')
year_list = []
count_list = []

YEAR_INDEX = 0
COUNTRY_INDEX = 5
MF_INDEX = 6
CATEGORY_INDEX = 2
EVENT_INDEX = 3
years = {}
with open('summer.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        mf = row[MF_INDEX]
        event = row[EVENT_INDEX]
        country = row[COUNTRY_INDEX]
        if country == name and event == 'Swimming':
            dt = int(row[YEAR_INDEX])
            full_date = datetime.date(dt, 1, 1)
            if not years.get(full_date):
                years[full_date] = 0
            years[full_date] += 1

year_list = sorted(years)
count_list = []
for y in year_list:
    count_list.append(years[y])
    print(str(y) + ": " + str(years[y]))
