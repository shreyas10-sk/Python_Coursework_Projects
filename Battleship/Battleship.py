# ITSS / OPRE 3311 – Introduction to Programming 
# Project: Battleship Game 
# Student Name: Shreyas Kanagal
# Date Completed: 03/02/2025
 
# Import necessary modules 
import random

# Display intro message 
print("Welcome to Battleship! Test your mettle!")
print("Your goal is to sink all the battleships on the board.")
print("Enter the row and column numbers to make your guess.")
print("Good luck!")
    
# Print the game board using a for loop 
def print_board(board):
    for row in board:
        print(" ".join(row))

# Place the ships randomly on the board using a while loop and selection statement 
def place_ships(board_size, num_ships):
    ships = {} 
    while len(ships) < num_ships:
        ship_row = random.randint(0, board_size - 1)
        ship_col = random.randint(0, board_size - 1)
        if (ship_row, ship_col) not in ships:
            ships[(ship_row, ship_col)] = False #Marking the ship as not hit
    return ships

# Initialize the game board and ships 
board_size = 5
num_ships = 3
board = [['O'] * board_size for _ in range(board_size)] 
ships = place_ships(board_size, num_ships) 
guesses = []

# Initialize counters for attempts and hits 
attempts = 0 
hits = 0 

print_board(board)

# Start main game loop 
while hits < num_ships: 
    try: 
        # Prompt user for their guess 
        guess_row = int(input("Guess Row (1-5): ")) 
        guess_col = int(input("Guess Column (1-5): ")) 
    except ValueError: 
        print("Invalid input. Please enter numbers between 1 and 5.") 
        continue 
    guess_row -= 1
    guess_col -= 1
        
    # Check if the guess is valid and not a duplicate 
    if (guess_row, guess_col) in guesses: 
        print("You already guessed that location. Try again.") 
    elif 0 <= guess_row < board_size and 0 <= guess_col < board_size: 
        attempts += 1 
        guesses.append((guess_row, guess_col)) 

        # Check if the guess is a hit or miss 
        if (guess_row, guess_col) in ships: 
            print("Hit!") 
            hits += 1 
            ships[(guess_row, guess_col)] = True 
            board[guess_row][guess_col] = 'X' 
        else: 
            print("Miss!") 
            board[guess_row][(guess_col)] = '-' 
    else: 
        print("Invalid input. Please enter numbers between 1 and 5.") 

# Print the game board after each guess
    print_board(board)

# End game and display results
print(f"Congratulations! You sank all {num_ships} battleships in {attempts} attempts!")
