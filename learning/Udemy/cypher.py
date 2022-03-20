letters = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!',
  ',','.','@','#','$','%','^','&','*','(',')','>','<','/',';','"','`','~',
  '{','}','|','?','_','-','+','=',':','1','2','3','4','5','6','7','8','9','0',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

task = str(input('What would you like to do: encrypt | decrypt\n> ')).lower()
text = str(input('\nType your message.\n> '))
rot = int(input('\nType the rotation number. 1-91\n> '))

if task == 'encrypt':
    encrypt(text, rot)
elif task == 'decrypt':
    decrypt(text, rot)
else:
    print('You did not enter a valid task.')

def encrypt(text, rot):
    encrypted_text = ''
    for letter in text:
        if letter not in letters:
            encrypted_text += letter
        else:
            position = letters.index(letter)
            new_index = position + rot
            if new_index >= len(letters):
                new_index = new_index - len(letters)
            encrypted_text += letters[new_index]
    print(f'\nyour encrypted message is:\n\n{encrypted_text}\n')

def decrypt(text, rot):
    decrypted_text = ''
    for letter in text:
        if letter not in letters:
            decrypted_text += letter
        else:
            position = letters.index(letter)
            new_index = position - rot
            if new_index >= len(letters):
                new_index = new_index + len(letters)            
            decrypted_text += letters[new_index]
    print(f'\nYour decrypted message is:\n\n{decrypted_text}\n')

