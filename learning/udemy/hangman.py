import random
import hangmanArt

def generate_blank_word(word):
    for i in range(len(word)):
        blank_word.append('_')
    print(' '.join(blank_word))
word_list = ['python', 'javascript', 'bananas', 'monkey','table', 'orange', 'russia', 'guide', 'certification']
word = random.choice(word_list)
blank_word = []
print(hangmanArt.logo)
generate_blank_word(word)

lives = 0
end_of_game = False

while not end_of_game:
    letter = input('Guess a letter:\n> ').lower()
    
    for num in range(len(word)):
        if word[num] == letter:
            if letter in blank_word:
                print(f'You have already guessed the letter {letter}. Try again!\n')
            blank_word[num] = letter
    print(f"""
    
    {' '.join(blank_word)}

    """)

    if letter not in word:
        lives += 1
        print(hangmanArt.hangman[lives])

    if lives and word == ''.join(blank_word):
        end_of_game = True
        print('You Win!')
    elif lives == 6:
        end_of_game = True
        print('You lost!')
