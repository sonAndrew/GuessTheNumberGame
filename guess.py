# This is a Guess the Number game.
import random
guessesTaken = 0

print('Hello! What is your name?')
playerName = input()

number = random.randint(1, 20)
print('Well, ' + playerName + ', I am thinking of a number between 1 and 20.')

for i in range(6):
    print('Take a guess.') # Four spaces in front of "print"
    guess = input()
    guess = int(guess)
    guessesTaken += 1

    if guess < number:
        print('Your guess is too low ' + playerName + '.') # Eight spaces in front of "print"

    if guess > number:
        print('Your guess is too high ' + playerName + '.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')