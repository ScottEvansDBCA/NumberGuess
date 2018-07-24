''' Guess the number!
    A random number will appear, users will have to guess what it is.
    After every guess a user will recieve HIGHER or LOWER as a hint.'''

import random

def generate_number():
    secret_number = random.randint(0,10)
    return secret_number

secret_number = generate_number()

def main():
    winning_number = secret_number
    print("The game has a picked a secret number between 0 and 10.\nCan you guess what it is?")
    while winning_number == secret_number:
        guess = input("Please enter your guess: ")
        higher_or_lower(guess)

def higher_or_lower(guess):
    global secret_number
    if guess < secret_number:
        print('Higher')
    elif guess > secret_number:
        print('Lower')
    else:
        print('Congratulations, you win!')
        secret_number = generate_number()
        play_again = raw_input("Would you like to play again? Y/N: ")
        if play_again.upper() == 'Y':
           main()
        else:
            pass

main()
