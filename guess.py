# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
playerName = input()

print('\nThanks for playing ' + playerName + '.')
print("\nHow to play: This is a guess the number terminal game. You choose your difficulty from EASY to EXTREME. You then guess a random number between two numbers, including those numbers. That's all.")

print('\nNOW CHOOSE YOUR DIFFICULTY!')

easy = 'Easy'
hard = 'Hard'
extreme = 'Extreme'

print('\nEnter your difficulty: ' + easy + ", " + hard + ', or ' + extreme)
difficulty = input()

if difficulty == extreme:
    number = random.randint(1, 20)
    print('\nWell, ' + playerName + ', I am thinking of a number between 1 and 20.')

    for i in range(6):
        print('\nTake a guess.') # Four spaces in front of "print"
        guess = input()
        guess = int(guess)
        guessesTaken += 1

        if guess < number:
            print('\nYour guess is too low ' + playerName + '.') # Eight spaces in front of "print"

        if guess > number:
            print('\nYour guess is too high ' + playerName + '.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('\nGood job, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('\nNope. The number I was thinking of was ' + number + '.')
elif difficulty == hard:
    number = random.randint(1, 10)
    print('\nWell, ' + playerName + ', I am thinking of a number between 1 and 10.')

    for i in range(4):
        print('\nTake a guess.') # Four spaces in front of "print"
        guess = input()
        guess = int(guess)
        guessesTaken += 1

        if guess < number:
            print('\nYour guess is too low ' + playerName + '.') # Eight spaces in front of "print"

        if guess > number:
            print('\nYour guess is too high ' + playerName + '.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('\nGood job, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('\nNope. The number I was thinking of was ' + number + '.')
elif difficulty == easy:
    number = random.randint(1, 5)
    print('\nWell, ' + playerName + ', I am thinking of a number between 1 and 5.')

    for i in range(2):
        print('\nTake a guess.') # Four spaces in front of "print"
        guess = input()
        guess = int(guess)
        guessesTaken += 1

        if guess < number:
            print('\nYour guess is too low ' + playerName + '.') # Eight spaces in front of "print"

        if guess > number:
            print('\nYour guess is too high ' + playerName + '.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('\nGood job, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('\nNope. The number I was thinking of was ' + number + '.')
else:
    print('Sorry somthing went wrong! You did not enter the difficulty level correctly.')