"""
    File: guess.py
    About: This a Guess the Number game.
"""
# Imports: EasyFrame, random
from breezypythongui import EasyFrame
import random



# Start of program

# Ask for player name.
print('\nHello! What is your name?')
playerName = input('\nEnter name here: ')

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# How to play.
print('\nThanks for playing ' + playerName + '.')
print("\nHow to play: This is a guess the number terminal game. You choose your difficulty from EASY to EXTREME. You then guess a random number between two numbers, including those numbers. That's all.")

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def guessTheNumber():
    guessesTaken = 0 # Guesses Taken Variable
    
    # Ask if player wants to start game.
    print('\n' + playerName + '. Do you want to start the game?')

    yes = "y"
    no = "n"

    beginProgram = input('\nEnter "y or n" ')

    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # While beginProgram input is a yes or no answer, enter game.
    while (beginProgram == yes or beginProgram == no):
        # If beginProgram input is "yes" ask for difficulty.
        if beginProgram == yes:
            easy = 'Easy'
            hard = 'Hard'
            extreme = 'Extreme'
            exit = 'Exit'

            # Ask for play difficulty level or if they want to exit game.
            print('\nNOW CHOOSE YOUR DIFFICULTY!')

            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

            print('\nEnter your difficulty: ' + easy + ", " + hard + ', or ' + extreme + ', or ' + exit)
            difficulty = input('Difficulty: ')

            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

            # If difficulty level is extreme.
            if difficulty == extreme:
                number = random.randint(1, 20)
                print('\nWell, ' + playerName + ', I am thinking of a number between 1 and 20.')
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                # Determine if guess is too high or low and calculate the number of guesses taken.
                for i in range(6):
                    print('\nTake a guess.')

                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                    guess = input()
                    guess = int(guess)
                    guessesTaken += 1

                    # If guess is too low notify player "Your guess is too low."
                    if guess < number:
                        print('\nYour guess is too low ' + playerName + '.')

                        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                    # If guess is too high notify player "Your guess is too high."
                    if guess > number:
                        print('\nYour guess is too high ' + playerName + '.')

                        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                    # If guessed correctly exit
                    if guess == number:
                        break
                
                # If guessed correctly notify play that they have guessed correctly.
                if guess == number:
                    guessesTaken = str(guessesTaken)
                    print('\nGood job, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!')

                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                # If guesses taken is not the number and they exhausted all tries, notify they have not guessed correctly.
                if guess != number:
                    number = str(number)
                    print('\nNope. The number I was thinking of was ' + number + '.')

                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                # Ask player if they want to contiue playing.
                print('\nDo you want to continue playing?')
                continuePlaying = input('\nEnter y or n. ')

                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                if continuePlaying == yes:
                    continue
                if continuePlaying == no:
                    exit
                else:
                    print('\nDo you want to continue playing?')
                    continuePlaying = input('\nEnter y or n. ')

            # If difficulty level is hard.
            elif difficulty == hard:
                number = random.randint(1, 14)
                print('\nWell, ' + playerName + ', I am thinking of a number between 1 and 14.')
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                # Determine if guess is too high or low and calculate the number of guesses taken.
                for i in range(4):
                    print('\nTake a guess.')

                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                    guess = input()
                    guess = int(guess)
                    guessesTaken += 1

                    # If guess is too low notify player "Your guess is too low."
                    if guess < number:
                        print('\nYour guess is too low ' + playerName + '.')

                        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                    # If guess is too high notify player "Your guess is too high."
                    if guess > number:
                        print('\nYour guess is too high ' + playerName + '.')

                        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                    # If guessed correctly exit
                    if guess == number:
                        break
                
                # If guessed correctly notify play that they have guessed correctly.
                if guess == number:
                    guessesTaken = str(guessesTaken)
                    print('\nGood job, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!')

                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                # If guesses taken is not the number and they exhausted all tries, notify they have not guessed correctly.
                if guess != number:
                    number = str(number)
                    print('\nNope. The number I was thinking of was ' + number + '.')

                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                # Ask player if they want to contiue playing.
                print('\nDo you want to continue playing?')
                continuePlaying = input('\nEnter y or n. ')

                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                if continuePlaying == yes:
                    continue
                if continuePlaying == no:
                    exit
                else:
                    print('\nDo you want to continue playing?')
                    continuePlaying = input('\nEnter y or n. ')

            # If difficulty level is easy.
            elif difficulty == easy:
                number = random.randint(1, 7)
                print('\nWell, ' + playerName + ', I am thinking of a number between 1 and 7.')
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                # Determine if guess is too high or low and calculate the number of guesses taken.
                for i in range(2):
                    print('\nTake a guess.')

                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                    guess = input()
                    guess = int(guess)
                    guessesTaken += 1

                    # If guess is too low notify player "Your guess is too low."
                    if guess < number:
                        print('\nYour guess is too low ' + playerName + '.')

                        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                    # If guess is too high notify player "Your guess is too high."
                    if guess > number:
                        print('\nYour guess is too high ' + playerName + '.')

                        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                    # If guessed correctly exit
                    if guess == number:
                        break
                
                # If guessed correctly notify play that they have guessed correctly.
                if guess == number:
                    guessesTaken = str(guessesTaken)
                    print('\nGood job, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!')

                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                # If guesses taken is not the number and they exhausted all tries, notify they have not guessed correctly.
                if guess != number:
                    number = str(number)
                    print('\nNope. The number I was thinking of was ' + number + '.')

                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                # Ask player if they want to contiue playing.
                print('\nDo you want to continue playing?')
                continuePlaying = input('\nEnter y or n. ')

                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                if continuePlaying == yes:
                    continue
                if continuePlaying == no:
                    exit
                else:
                    print('\nDo you want to continue playing?')
                    continuePlaying = input('\nEnter y or n. ')

            # If difficulty level is exit.
            elif difficulty == exit:
                quit()

            # If other value entered, notify player.
            else:
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('\nSorry somthing went wrong! You did not enter the difficulty level correctly.')
                
        # If beginProgram input is "no" ask if they are sure they want to end the game.
        elif beginProgram == no:
            print('\nAre you sure you want to end the game?')
            endGame = input('\nEnter "y" for yes, or "n" for no: ')
            
            if endGame == yes:
                quit()
            else:
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('\n' + playerName + '. Do you want to start the game?')
                beginProgram = input('\nEnter "y" for yes, or "n" for no: ')
    # Else if other value notify player they entered an incorrect value.
    else:
        print('\nSorry you entered the wrong value.')
        print('\n' + playerName + '. Do you want to start the game?')
        beginProgram = input('\nEnter "y" for yes, or "n" for no: ')

def main():
    guessTheNumber()

if __name__ == "__main__":
    main()