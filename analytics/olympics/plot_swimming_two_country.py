import csv
import pylab as pl
import datetime

name = input('What country are you interested in (e.g. USA? ')
year_list = []
count_list = []
name2 = input('What other country are you interested in (e.g. RUS? ')
year_list2 = []
count_list2 = []

YEAR_INDEX = 0
COUNTRY_INDEX = 5
MF_INDEX = 6
EVENT_INDEX = 3
years = {}
years2 = {}
with open('input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        mf = row[MF_INDEX]
        event = row[EVENT_INDEX]
        if row[COUNTRY_INDEX] == name and event == 'Swimming' and mf == 'Women':
            dt = int(row[YEAR_INDEX])
            if not years.get(dt):
                years[dt] = 0
            years[dt] += 1
        if row[COUNTRY_INDEX] == name2 and event == 'Swimming' and mf == 'Women':
            dt = int(row[YEAR_INDEX])
            if not years.get(dt):
                years[dt] = 0
            years2[dt] += 1

#            year_list2.append(datetime.date(dt, 1, 1))

sorted_names = sorted(years, key=years.get)

fig = pl.figure()
ax = pl.subplot(111)
p0 = pl.plot(year_list, count_list, label=name)
p1 = pl.plot(year_list2, count_list2, label=name2)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])

pl.savefig(name + name2 + '.pdf')
