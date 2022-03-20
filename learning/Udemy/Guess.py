from game_data import data
import random

game = True
userNum = 0

while game:
#pick random item from data
    A = random.choice(data)
    B = random.choice(data)
    compareNum = 0


    #Create String with data
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(f"Compare A: {B['name']}, a {B['description']}, from {B['country']}")


    guess = str(input('\nWho has more followers? A | B\n> ')).upper()

    if guess == 'A':
        userNum = A['follower_count']
        compareNum = B['follower_count']

    if guess == 'B':
        userNum = B['follower_count']
        compareNum = A['follower_count']

    #Debugging:
    print(userNum, compareNum)

    if userNum < compareNum:
        print('Congrats!')
    else:
        game = False


# print(guess['follower_count'])
