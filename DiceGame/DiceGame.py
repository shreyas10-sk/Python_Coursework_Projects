import random
import datetime

# ITSS/OPRE 3311 - Object-Oriented Programming
# Assignment 5: Dice Game Revisited
# Developer: Shreyas Kanagal
# Date: 2025-03-10

# Function to prompt for and read-in user name
def get_name():
    while True:
        try:
            name = input("Enter your name (just a single word, no spaces please!): ")
            if not name.isalpha():
                print ("You must enter a valid name.")
            else:
                return name 
        except ValueError:
            print ("You must enter a valid name.")

# Function to print welcome message and rules of the game
def welcome (name):
    print ("A warm and hearty welcome to the High Roller Dice game, ", name, "!\n")
    print ("Rules: Roll 3 dice. A pair (Doublet) earns 5 bonus points, and three of a kind (Triplet) earns 20! Your score is the sum of the dice plus any bonus points.\n")

# Function to get the number of games to be played
def get_games():
    while True:
        try:
            games = int(input("How many games would you like to play? "))
            if games <= 0:
                print ("You must enter a number greater than 0.")
            else:
                return games
        except ValueError:
            print ("You must enter a valid number. Please enter a valid integer.")

# Function to roll a single die
def roll_die():
    return random.randint(1, 6)

# Function to calculate bonus points
def calculate_bonus(die1, die2, die3):
    if die1 == die2 and die2 == die3:
        return 20
    elif die1 == die2 or die2 == die3 or die1 == die3:
        return 5
    else:
        return 0
    
# Function to get results based on bonus points
def get_results(bonus):
    if bonus == 20:
        return "You rolled a Triplet!"
    elif bonus == 5:
        return "You rolled a Doublet!"
    else:
        return "No bonus. Better luck next time, buddy."

# Function to prompt the use to play again
def play_again():
    while True:
        play = input("Would you like to play again? (y/n): ")
        if play.lower() == "y":
            return True
        elif play.lower() == "n":
            return False
        else:
            print ("Invalid input. You must enter 'y' or 'n'.")

# Function to print the outro message
def print_end_message(name):
    print ("Thank you for playing, ", name, "!")
    print ("Goodbye!")

# Function for the main game loop
def main():
    random.seed()
    name = get_name()
    welcome (name)

    while True:
        games = get_games()

        for _ in range(games):
            die1 = roll_die()
            die2 = roll_die()
            die3 = roll_die()

            dice = sorted([die1, die2, die3])
            die1, die2, die3 = dice

            bonus = calculate_bonus(die1, die2, die3)
            score = sum (dice) + bonus
            result = get_results(bonus)

            today = datetime.datetime.now()
            print ("You rolled: ", die1, die2, die3)
            print (f"Date: {today.strftime('%Y-%m-%d')} Time: {today.strftime('%H:%M:%S')}")
            print (f"Dice: {die1}, {die2}, {die3}")
            print (f"Result: {result}")
            print (f"Score: {score}\n")

        if not play_again():
            break
    
    print_end_message(name)

if __name__ == "__main__":
    main()
            