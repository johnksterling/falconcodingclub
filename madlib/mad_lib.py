name = input('Enter your name: ')
answer = 'yes'
while(answer == 'yes'):
    if answer.strip() == 'no':
        print('Goodbye {}'.format(name))
    else:
        madlib_1 = 'I went to'
        place = input('Enter a place: ')
        madlib_2 = 'on'
        day = input('Enter a day of the week: ')
        print('I went to {} on {}'.format(place, day))
    answer = input('would you like to keep playing {}?'.format(name))
