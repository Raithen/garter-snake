def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = int(input('What is the first number?\n> '))
num2 = int(input('What is the second number?\n> '))

for operation in operations:
    print(operation)
operation_symbol = input('Which operation would you like to do?\n> ')
operation = operations[operation_symbol]
total = operation(num1,num2)

print(f'{num1} {operation_symbol} {num2} = {total}')