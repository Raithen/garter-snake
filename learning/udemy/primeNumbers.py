def isPrimeNumber(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    
    if is_prime:
        print(f'{number} is a prime number!')
    else:
        print(f'{number} is not a prime number!')

#can only be divided by 1 and itself:
number = int(input('Enter a number: '))
isPrimeNumber(number)