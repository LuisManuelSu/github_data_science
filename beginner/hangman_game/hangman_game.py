# This is the famuous game "Hangman"
import random

# Function to select a word to be guessed. Can be automaticallz generated or type by the user
def select_word():
    while True:
        print('\nYou have the option of write a Word to be guessed for other user, \nor the word will be selected from a random List')
        user = input('Do you want to type the word to be guessed by other user (y/n)?\n>>>')
        if user.lower() == 'y':
            word = input('Type the Word to be guessed\n>>>').upper()
            return word
        elif user.lower() == 'n':
            print('\nThen, the word will be automatically generated')
            break
        else:
            print('\nInvalid Data: Enter "y" if you want to slect your own word, or "n" if you want that be randomly generated')
            continue
    with open('words.txt', 'r') as fileref:
        fileref = fileref.readlines()
        word = random.choice(fileref).rstrip().upper()
        # print(word)
        return word

# Function to create a status of the guessed "_L___ER N____N_L P_RK"
def path(word, guessed_list):
    guessing_path = ''
    for letter in word:
        if letter not in guessed_list:
            guessing_path += '_'
        else:
            guessing_path += letter
    return guessing_path

# Logic of the Game
def guessing():
    word = select_word()
    word_len = len(word)
    print('\nThe word you need to guess has {} letters'.format(word_len))
    print('You will have only 5 opportunities to fail')
    letter_guessed = []
    guessing_path = path(word, letter_guessed)
    print('Word: {}'.format(guessing_path))

    count = 0
    while count <= 5:
        # print(count)
        letter = input('Guess a Letter:\n>>>').upper() #user enter of guessing of each letter
        if len(letter) != 1:
            print('Invalid Entry. Type only a single letter')
            continue
        if letter not in letter_guessed:
            letter_guessed.append(letter)
            # print(letter_guessed) # testing the list of letters already guessed
            if letter in word:
                print('\nThe letter guessed is in the Word to guess')
                guessing_path = path(word, letter_guessed)
                print('Letters guessed so far: {}'.format(letter_guessed)) # testing that the "guessing list"
                print('Word: {}. You have {} fails'.format(guessing_path, count))
                if '_' not in guessing_path:
                    print('\nYou have guessed the Word. Congratullations {}!!! YOU WON!!!'. format(user_name))
                    break
                continue
            else:
                print('\nThe letter guessed is not in the Word to guess')
                count += 1
                print('Letters guessed so far: {}'.format(letter_guessed)) # testing that the "guessing list"
                print('Word: {}. You have {} fails'.format(guessing_path, count))
                if count == 6:
                    print('\nSorry, you have lost all your chances, the word was "{}". \nGAME OVER!!!'.format(word))
                continue
        else:
            print('\nYou already said this letter, try another one')

# Start the execution of the program asking to the user the name and if want to play
# The user can play several times without go out from the program
print('\nWelcome to the "Hangman Game"')
user_name = input('What is your name?\n>>>')
while True:
    user = input('\nHi {}, Do you want to play Hangman (y/n) \n>>>'.format(user_name))
    if user.lower() == 'y':
        guessing()
        continue
    elif user.lower() == 'n':
        print('See you later {}!!!'.format(user_name))
        break
    else:
        print('\nInvalid Data: Enter "y" if you want to play, or "n" if you want to go out')
        continue
