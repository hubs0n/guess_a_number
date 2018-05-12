import random

print('------------------------------------')
print('     GUESS THE NUMBER GAME')
print('------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input("What is your name? :")

while guess != the_number:
    guess_text = input('Guess the number between 0 and 100: ')
    guess = int(guess_text)


    if guess < the_number:
        print('{} your guess of {} is too Low'.format(name, guess))
    elif guess > the_number:
        print('{} your guess of {} is too High'.format(name, guess))
    else:
        print('Congratulations {} you won with guessing {}!'.format(name, guess))

print('Done')