import random

names = input('Who is going to pay the Bill today? You can enter names followed by a Comma and space.\n> ').split(', ')
print(names)


randomNum = random.randint(0,len(names) -1)
print(randomNum)
print(f'{names[randomNum]} will pay the bill!')