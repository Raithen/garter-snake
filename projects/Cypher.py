lc_alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uc_alpha = [letter.upper() for letter in lc_alpha]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [" ", ",", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "{", "[", "}", "]", "\\", "|", ":", ";", '"', "'", "<", ",", ">", ".", "/", "?"]
letters = []

keys = [symbols, lc_alpha, uc_alpha, numbers]
for list in keys:
    letters += [letter for letter in list]


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

print("""
   ______            __                      ____ 
  / ____/_  ______  / /_  ___  _____   _  __/ __ \\
 / /   / / / / __ \/ __ \/ _ \/ ___/  | |/_/ /_/ /
/ /___/ /_/ / /_/ / / / /  __/ /     _>  < \__, / 
\____/\__, / .___/_/ /_/\___/_/     /_/|_|/____/  
     \____/_/        SIMEPLE MESSAGE ENCRYPTION                                                       
                
""")

task = input('What would you like to do: encrypt | decrypt | quit \n> ').lower()

if task != 'quit':
    text = str(input('\nType your message.\n> '))
    rot = int(input(f'\nType the rotation number. 1-{len(letters)-1}\n> '))
    if task == 'encrypt':
        encrypt(text, rot)
    elif task == 'decrypt':
        decrypt(text, rot)
    else:
        print('You did not enter a valid task.')
else:
    print('Exiting Program.')