''' Guess the number!
    A random number will appear, users will have to guess what it is.
    After every guess a user will recieve HIGHER or LOWER as a hint.'''

import random

def generate_number():
    secret_number = random.randint(0,10)
    return secret_number

secret_number = generate_number()

def higher_or_lower(guess):
    global secret_number
    if guess < secret_number:
       print('Higher')
    elif guess > secret_number:
       print('Lower')
    else:
       print('Congratulations, you win! Guess again to restart.')
       secret_number = generate_number()
