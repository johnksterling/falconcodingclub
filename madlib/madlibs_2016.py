import random

keep_playing = True
madlibs = []
madlibs.append("I would like to {verb} at the {place}")
madlibs.append("When I was a child a was afraid to {verb} at the {place}")
madlibs.append("Is the {place} where you like to {verb}")

while keep_playing:
    madlib = random.choice(madlibs)
    verb = input('enter a verb: ')
    place = input('enter a place: ')
    print(madlib.format(verb=verb, place=place))
    answer = input('Would you like to play again?')
    if answer == 'no':
        keep_playing = False
