import random

keep_playing = True
madlibs = []
madlibfile = open('madlibs.txt', 'r')
madlib = madlibfile.readline().strip()
while madlib:
    madlibs.append(madlib)
    madlib = madlibfile.readline().strip()
while keep_playing:
    madlib = random.choice(madlibs)
    verb = input('enter a verb: ')
    place = input('enter a place: ')
    print(madlib.format(verb=verb, place=place))
    answer = input('Would you like to play again?')
    if answer == 'no':
        keep_playing = False
