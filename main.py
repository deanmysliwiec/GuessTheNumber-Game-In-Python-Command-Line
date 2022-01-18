# Guess the number game
# Made by Dean Mysliwiec

import random

# global variable won
won = False


# comparing user's guess to comp's guess and returning value
def userGuess(guess, comp):
    if guess > comp:
        return 0
    elif guess < comp:
        return 1
    elif guess == comp:
        return 2
    else:
        return 3  # will never return 3


# comparing statements based on userGuess function's return value
def statements(num):
    if num == 0:
        print("Number is lower...")
    elif num == 1:
        print("Number is higher...")
    elif num == 2:
        youWon()


# display if won
def youWon():
    print("\nYou have won!")
    global won
    won = True


# display if lost
def youLost(comp):
    print(f"\nYou have lost...The number was {comp}")


# main game
def guessTheNumber():
    global won
    won = False

    # while loop variable
    end = "n"

    # beginning statement
    print("--- Welcome to the Guess the Number Game! ---\n")
    print("I'm thinking of a number between 1 and 100...\n")
    print("Easy Difficulty = 10 lives, Hard Difficulty = 5 lives\n")

    while end != "y":
        # lives variable created
        lives = -1
        # while lives is less than 0, unless difficulty is chosen
        while lives < 0:
            difficulty = input("\nChoose a difficulty (easy/hard): ").lower()
            if difficulty == "easy":
                lives = 10  # 10 lives
            elif difficulty == "hard":
                lives = 5  # 5 lives
        # get random number choice 1-100
        comp_choice = random.randint(1, 101)

        # while lives is not 0 and won doesn't equal True
        while lives != 0 and won is not True:
            print(f"\nYou have {lives} lives left.")
            # ask for user's guess
            users_guess = int(input("\nWhat is your guess? "))
            # compare via userGuess
            compare = userGuess(users_guess, comp_choice)
            # get statement based on value of compare
            statements(compare)
            lives -= 1
            # if lives greater than 0 and the user's guess has not won the game
            if lives > 0 and comp_choice != users_guess:
                print("Guess again...")
            # if lives is 0 then user lost
            elif lives == 0:
                youLost(comp_choice)
            # display nothing if conditions not met
            else:
                print()

        # variable used as condition in while loop
        y = True
        # check if user wants to play again
        while y:
            ask = input("\nWould you like to play again? (Y/N): ").lower()
            if ask == "n":
                end = "y"
                y = False
                print("\nGoodbye! Thanks for playing!")
            elif ask == "y":
                end = "n"
                won = False
                y = False
            else:
                print("\nPlease enter a valid input.")


# start the game
guessTheNumber()
