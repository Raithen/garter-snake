fruits = ["Strawberries", "Nectarines","apples","grapes","peaches","Cherries",'Pears']
vegetables = ['carrtos', "Potatoes", 'lettuce', 'kale', 'tomatoes']

dirty_dozen = [fruits, vegetables]

for item in dirty_dozen:
    for i in range(len(item)):
        print(item[i])
        