import random
print('Welcome to Rock Paper Scissor Game')
print('Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock')
#list of options
options = ['Rock', 'Paper', 'Scissor']
user_choice = input('Enter your choice (Rock/Paper/Scissor): ')
computer_choice = random.choice(options)
if user_choice == computer_choice:
    print('Match tied')
elif user_choice == 'Rock':
    if computer_choice == 'Paper':
        print('Computer won Paper beats Rock')
    else:
        print('You won Rock beats Scissors')
elif user_choice == 'Paper':
    if computer_choice == 'Rock':
        print('You won Paper beats Rock')
    else:
        print('Computer won Scissors beats Paper')
elif user_choice == 'Scissor':
    if computer_choice == 'Rock':
        print('Computer won Rock beats Scissor')
    else:
        print('You won Scissors beats Paper')
else:
    print('In-valid Option Try again!')