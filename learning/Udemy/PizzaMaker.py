print('Welcome to Pizza Pies!')
pizza_size = input('What size pizza would you like: S, M or L?\n> ').upper()
pizza_cost = 0

if pizza_size == 'S':
    pizza_cost = 5
elif pizza_size == 'M':
    pizza_cost = 10
elif pizza_size == 'L':
    pizza_cost = 15

if pizza_cost > 0:
    add_pepperoni = input('Would you like Pepperonis: Y or N?\n> ').upper()
    extra_cheese = input('Would you like Extra Cheese: Y or N?\n> ').upper()

    if add_pepperoni == 'Y':
        pizza_cost += 3

    if extra_cheese == 'Y':
        pizza_cost += 3
        
    print(f'Your total is ${pizza_cost}!')
else:
    print('You did not enter a pizza size!')
