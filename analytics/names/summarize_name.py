import csv

name = input('What name would you like to search? ')

NAME_INDEX = 1
YEAR_INDEX = 2
COUNT_INDEX = 4
with open('input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        year = row[YEAR_INDEX]
        count = row[COUNT_INDEX]
        if row[NAME_INDEX] == name:
            print(year + ': ' + count)
