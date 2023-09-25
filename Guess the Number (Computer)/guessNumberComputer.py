import random

def guess(x):
    randomNumber = random.radint(1, 100) 
    guess = 0
    while guess != randomNumber:
        guess = (input(f'Guess a number between 1 and {x}: '))
        if guess < randomNumber:
            print('Sorry. Too low. ')
        elif guess > randomNumber:
            print('Sorry. Too hight. ')

    print(f'Good job, You have guessed the number {randomNumber}: correctly! ')

def computerGuess(x):
    low = 1
    high = 100
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == '1':
            low = guess + 1

    print(f'Nice, The computer guessed your number, {guess}, correctly! ')        

computerGuess(100)