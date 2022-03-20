# 2000 / 4 = 500 : Leap
# 2000 / 100 = 20 : Not Leap
# 2000 / 400 = 5 : Leap
year = int(input('Enter a Year: '))
if year % 4 == 0:
    if year % 400 == 0:
        print('Leap year!')
    elif year % 100 == 0:
        print('Not a Leap Year!')
    else:
        print('Leap Year!')
else:
    print('Not a Leap Year!')