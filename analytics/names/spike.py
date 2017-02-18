import csv
year_names = {}
with open('input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        if not year_names.get(int(row[2])):
            year_names[int(row[2])] = {}
        year_names[row[2]][row[1] = int(row[4])
        

for year in year_names
sorted_names = sorted(female_names, key=female_names.get)
for name in sorted_names:
    
