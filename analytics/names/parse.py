import csv

male_names = {}
female_names = {}
with open('input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        dict_to_use = male_names if row[3] == 'M' else female_names
        if dict_to_use.get(row[1]):
            dict_to_use[row[1]] += int(row[4])
        else:
            dict_to_use[row[1]] = int(row[4])

sorted_names = sorted(female_names, key=female_names.get)
top5 = sorted_names[0:10]
bottom5 = sorted_names[-10:]
for name in top5:
    print(name + ': ' + str(female_names[name]))
for name in bottom5:
    print(name + ': ' + str(female_names[name]))

