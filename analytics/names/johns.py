import csv
import pylab as pl
import datetime

name = input('What name are you interested in? ')
male_or_female = input('N, M or F? ')
name2 = input('Another name are you interested in? ')
male_or_female2 = input('N, M or F? ')
year_list = []
count_list = []
year_list2 = []
count_list2 = []

years = {}
with open('input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        if row[1] == name and (male_or_female == 'N' or row[3] == male_or_female):
            dt = int(row[2])
            years[dt] = int(row[4])
            year_list.append(datetime.date(dt, 1, 1))
            count_list.append(int(row[4]))
        if row[1] == name2 and (male_or_female == 'N' or row[3] == male_or_female2):
            dt = int(row[2])
            years[dt] = int(row[4])
            year_list2.append(datetime.date(dt, 1, 1))
            count_list2.append(int(row[4]))

sorted_names = sorted(years, key=years.get)

fig = pl.figure()
ax = pl.subplot(111)
p0 = pl.plot(year_list, count_list, label=name)
p1 = pl.plot(year_list2, count_list2, label=name2)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])

pl.savefig(name + name2 + '.pdf')
