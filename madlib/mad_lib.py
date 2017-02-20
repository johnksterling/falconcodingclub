name = input('Enter your name: ')
answer = 'yes'
madlib_template = 'I went to {} on {}'
while(answer.strip().lower() == 'yes'):
    place = input('Enter a place: ')
    day = input('Enter a day of the week: ')
    print(madlib_template.format(place, day))
    answer = input('would you like to keep playing, {}? '.format(name))
print('Goodbye {}'.format(name))
