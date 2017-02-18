import csv
import pylab as pl
import datetime


def plot_graph(filename, x_axis, y_axis):
    ax = pl.subplot(111)
    pl.plot(year_list, count_list, label=name)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])
    pl.savefig(filename + '.pdf')

name = input('What country are you interested in (e.g. USA)? ')
year_list = []
count_list = []

YEAR_INDEX = 0
COUNTRY_INDEX = 5
MF_INDEX = 6
EVENT_INDEX = 3
years = {}
with open('summer.csv', 'r') as csvfile:
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
plot_graph(name, year_list, count_list)

