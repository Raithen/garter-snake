import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '=', '+']
numbers = [1,2,3,4,5,6,7,8,9,0]
password = []
random_pass = []
print("""
Password Generator
 .--.  
/.-. '----------.
\\'-' .--"--""-"-'
 '--'
""")
letter_qty = int(input('How many Letters would you like?\n> '))
symbols_qty = int(input('How many Symbols would you like?\n> '))
numbers_qty = int(input('How many Numbers would you like?\n > '))

#Pick Random Letters
for num in range(0,letter_qty):
    random_letter = letters[random.randint(0,len(letters)-1)]
    password.append(random_letter)

for num in range(0, symbols_qty):
    random_symbol = symbols[random.randint(0, len(symbols)-1)]
    password.append(random_symbol)

for num in range(0, numbers_qty):
    random_number = numbers[random.randint(0, len(numbers)-1)]
    password.append(str(random_number))

#generate password
for num in range(0,len(password)):
    random_char = password[random.randint(0,len(password) -1)]
    random_pass.append(random_char)
    password.remove(random_char)

print(f"""

Here is your Random Password.
Don't lose it!

{''.join(random_pass)}
""")