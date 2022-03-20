row1 = ['☐','☐','☐']
row2 = ['☐','☐','☐']
row3 = ['☐','☐','☐']

map = [row1, row2, row3]
print(f'{map[0]}\n{map[1]}\n{map[2]}')

xMark = input('''
where would you like to place the treasure?
Enter two numbers: Column, Row
Example: 22 
> ''')

col = int(xMark[0]) -1
row = int(xMark[1]) -1

map[row][col] = 'X'
print(f'{map[0]}\n{map[1]}\n{map[2]}')