# Guessing Game human user. In this game a user should guess a number between 1 to 100. The name_user
# will have six (6) opportunities to guess the number.

import random

def guess_number():
  # Introduction to the user
    name_user = input('Hello, welcome to the "Guessing Number Game". \nWhat is your name: \n>>>')
    print("Nice to meet you {}. Let's play..".format(name_user))
    print("The idea of the game is to guess a number between 1 and 100 in less tha 6 attempts. \nLet's start")
    # randomize the number to guess
    number_to_guess = random.randint(1,100)
    count = 1
    while True:
        if count <= 6:
            guess = input("\nWhat number you want to select: \n>>>")
            try:
                guess_numb = int(guess)
            except Exception:
                print('Your selection is not valid. Please select a number between 1 and 100')
                continue
            # Number not in the range
            if guess_numb < 1 or guess_numb > 100:
                print('Your selection is not valid. Please select a number between 1 and 100')
                continue
            # Numer greater than the number to guess
            elif guess_numb > number_to_guess:
                print('Your selection is greater than the number to guess. try Lower')
            elif guess_numb < number_to_guess:
                print('Your selection is lower than the number to guess. try Higher')
            else:
                print('You did it {}. You guess the number in {} attempt(s)'.format(name_user, count))
                break
            count += 1
        else:
            print('\n"GAME OVER"\n')
            print('I am sorry {}, but that was your last attempt. Please, try it again.'. format(name_user))
            break

guess_number()
