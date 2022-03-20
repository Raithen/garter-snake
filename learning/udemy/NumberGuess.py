import random
random_number = random.randint(1,100)

print('''Welcome to the number guessing game!
I'm thinking of a number between 1 and 100.''')
game_mode = input('Choose a difficulty. easy | hard\n> ').lower()

if game_mode == 'easy':
    attempts = 10
elif game_mode == 'hard':
    attemps = 5
else: 
    print('You didn\'t type easy or hard!')
    break