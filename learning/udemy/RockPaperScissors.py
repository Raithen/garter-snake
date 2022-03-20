import random

game = ['Rock','Paper','Scissors']

userGuess = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n> '))
computerGuess = random.randint(0,2)

userPlay = game[userGuess]
computerPlay = game[computerGuess]

print(f'User picked: {userPlay}')
print(f'Computer Picked: {computerPlay}')

if userPlay == computerPlay:
    print('It\'s a Draw!')

if userPlay == 'Rock' and computerPlay == 'Scissors':
    print('You Win!')