user_selection = input("Enter R, P, or S: ")
possible_options = ["R", "P", "S]
computer_option = random.choice(possible_options)
print("Computer selected: ", computer option)
output = ""
if user_selection == computer_selection:
    output = "Draw"      
elsif user_selection == 'R':
    if computer_selection == 'S':
        output = "You Win"
    else:
        output = "Computer Wins, Sorry!"
elsif user_selection == 'P':
    if computer_selection == 'R':
        output = "You Win"
    else:
        output = "Computer Wins, Sorry!"
elsif user_selection == 'S':
    if computer_selection == 'P':
        output = "You Win"
    else:
        output = "Computer Wins, Sorry!"
    
