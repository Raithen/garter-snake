import pprint
#Get word to count letter occurances
message = str(input('What is the word?\n> '))

count = {};

for character in message.lower():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)