from os import system, name

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
task = ''


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


def print_report(inventory):
    print("Here is what is currently in inventory:\n")
    for item in inventory:
        print(f"{item}: {inventory[item]}")


def print_menu(menu):
    print("Here is what's currently on the menu:\n")
    for item in menu:
        print(f"{item.title()}: ${menu[item]['cost']}")
    print("\n")


def check_resources(requested_item, inventory):
    for ingredient in MENU[requested_item]["ingredients"]:
        qty = MENU[requested_item]["ingredients"][ingredient]

        if inventory[ingredient] < qty:
            print(f"There is not enough {ingredient} to make your {requested_item.title()}.")
            return False
    return True


def accept_payment(requested_item, inventory):
    clear()
    cost = MENU[requested_item]["cost"]
    total = 0
    change = 0
    print(f"The cost of your {requested_item.title()} is ${cost}.\n")
    quarters = int(input("How many quarters\n> ")) *.25
    dimes = int(input("How many dimes\n> ")) * .10
    nickles = int(input("How many nickles\n> ")) * .05
    pennies = int(input("How many pennies\n> ")) * .01
    total += round(quarters + dimes + nickles + pennies, 2)
    clear()
    print(f"You entered ${total}")
    if total > cost:
        change = total - cost
        change = round(change, 2)
        inventory["money"] += cost
        return change
    else:
        print("You did not enter enough money!")
        return False


def make_drink(requested_item, inventory):
    for ingredient in MENU[requested_item]["ingredients"]:
        qty = MENU[requested_item]["ingredients"][ingredient]

        inventory[ingredient] -= qty


def refill(inventory):
    print_report(inventory)
    refill_item = input("\nPlease select the item you want to refill\n> ")
    refill_qty = int(input("\nPlease enter the amount you would like to add.\n> "))

    if refill_qty > 0:
        inventory[refill_item] += refill_qty
        print_report(inventory)


print("""
    Welcome to the Coffee Machine! What would you like to do?
    Drink | Report | Refill | Off
    """)
task = input("> ").lower()

while task != "off":

    if task == "drink":
        clear()
        print_menu(MENU)
        item = input('What drink would you like to order?\n> ').lower()
        enough_resources = check_resources(item, resources)

        if enough_resources:
            change = accept_payment(item, resources)
            if change:
                clear()
                make_drink(item, resources)
                print(f"Here is your {item.title()} and ${change} in change.")
        task = input("\nWhat would you like to do?\nDrink | Report | Refill | Off\n> ")

    elif task == "report":
        clear()
        print_report(resources)
        task = input("\nWhat would you like to do?\nDrink | Report | Refill | Off\n> ")
    elif task == "refill":
        clear()
        refill(resources)
        task = input("\nWhat would you like to do?\nDrink | Report | Refill | Off\n> ")
    else:
        clear()
        print("You did not enter a valid command!")
        task = input("\nWhat would you like to do?\nDrink | Report | Refill | Off\n> ")
clear()
print("Coffee Machine Shutting Down..")