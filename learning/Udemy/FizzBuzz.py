#Divisiable by 3: Fizz
#Divisable by 5: Buzz
#Divizable by 3 &5: FizzBuzz

for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz!')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)