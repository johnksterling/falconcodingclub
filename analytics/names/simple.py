import csv

NAME_INDEX = 1
YEAR_INDEX = 2
MF_INDEX = 3
COUNT_INDEX = 4
with open('input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        if row[NAME_INDEX] == 'Eleanor' and row[MF_INDEX] == 'F':
            print(row[YEAR_INDEX] + ': ' + row[COUNT_INDEX])
