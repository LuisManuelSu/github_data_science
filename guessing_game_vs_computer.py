# Guessing Game human user vs computer. The user should write the range (minimum and maximum) to guess a
# number in that range. After the user guess the number, the computer will do it. Who do it in less guesses
# will win the game 

import random

# Definition of the Function to guess the number
def random_game(min_number=1, max_number=100):

    random_number = random.randrange(min_number, max_number + 1) # Generate a random number between 1 and 100
    user = 0 # Initialize the user guess variable
    comp = 0 # Initialize the computer guess variable
    count_user = 0
    count_comp = 0
    # The user guess part
    while user != random_number:
        count_user = count_user + 1
        user = int(input('Enter your guess between {} and {}: '.format(min_number, max_number))) # Ask the user for a random number between 1 and 100
        print('Your guess is {}'.format(user))
        if user < random_number:
            print('Go higher')
        elif user > random_number:
            print('Go lower')
        else:
            print('\nYou guessed it!!!')
            print('You took {} steps to guess it'.format(count_user))
    # The computer guess part
    while comp != random_number:
        count_comp = count_comp + 1
        comp = random.randrange(min_number,max_number)
        if comp < random_number:
            min_number = comp
        elif comp > random_number:
            max_number = comp
        else:
            print('\nThe Computer took {} steps to guess it\n'.format(count_comp))

    if count_user < count_comp:
        print('Congratulations!!! you have beat the Computer')
    elif count_comp < count_user:
        print('The Computer has won the game. Keep Trying!!!')
    else:
        print("It's a Tie")

print('Define the range for the game') # Starting the Game
min_val = int(input('Minimum value: '))
max_val = int(input('Maximum value: '))
random_game(min_val, max_val) # Call of the function
