import random
import string
from words import words  # Make sure this file exists and has a list of words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ''.join(['a', 'b', 'cd']) -> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters ', ''.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✅ Correct!")
            else:
                lives = lives - 1 # takes away a life if wrong
                print("❌ Wrong letter.")
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:        
        print(f'\n🎉 You guessed the word {word}!')

# Run the game
hangman()
