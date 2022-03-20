from random import randint
randomNumber = randint(1,100)

# troubleshooting
# print(randomNumber)

#Set User Counter
EASY_MODE_TURNS = 10
HARD_MODE_TURNS = 5

def set_difficulty():
    print('Welcome to the Random Number Game!')
    difficulty = input('Pick your difficulty: easy | hard\n>').lower()

    if difficulty == 'easy':
        return EASY_MODE_TURNS
    elif difficulty == 'hard':
        return HARD_MODE_TURNS
    else:
        print('You did not select a difficulty! Easy it is.')
        return EASY_MODE_TURNS

counter = set_difficulty()

print(f"""You have {counter} attempts
to guess the random number between 1 and 100!\n""")


guess = int(input('What is your guess?\n> '))

while counter > 0:
    if guess == randomNumber:
        counter -= 1
        print(f'You guessed the correct number with {counter} attempts left!')
        break
    elif guess < randomNumber:
        counter -= 1
        print(f'Your guess was too low! You have {counter} attempts left. Try again.')
        guess = int(input('What is your guess?\n> '))
    elif guess > randomNumber:
        counter -= 1
        print(f'Your guess was too high! You have {counter} attempts left. Try again.')
        guess = int(input('What is your guess?\n> '))
