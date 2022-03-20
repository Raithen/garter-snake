# import sys

# name = input(str('What is your name?\n > '))
# print(f'Hello {name}, it\'s nice to finally meet you!')

# for i in name:
#     print(i)

# if len(name) < 5:
#     print('You have a short name!')
# elif len(name) > 5:
#     print('You have a long name!')
# else:
#     print('Your name is just right at 5 letter!')

def div42by(divideBy):
    try:
        return 42 /divideBy
    except ZeroDivisionError:
        print("Can't Device by Zero!")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))