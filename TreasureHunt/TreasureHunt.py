"""
ITSS 3311 Assignment 7: Treasure Hunt Game
Author: Shreyas Kanagal
Date: 4/7/2025
"""

import random

# Constants
GRID_SIZE = 5
NUM_TREASURES = 3
MOVES = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def initialize_game():
    """
    Initialize the game grid and player position
    Returns:
        tuple: (grid, player_position)
    """
    print("\nWelcome to the Treasure Hunt Game!")
    print(f"Navigate the {GRID_SIZE}x{GRID_SIZE} grid to find {NUM_TREASURES} hidden treasures.")
    print("Enter moves: up, down, left, right\n")
    
    grid = create_grid_with_treasures()
    player_position = (0, 0)
    return grid, player_position

def create_grid_with_treasures():
    """
    Create a grid with randomly placed treasures
    Returns:
        list: 2D list representing the game grid
    """
    grid = [['empty' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    treasures_placed = 0

    while treasures_placed < NUM_TREASURES:
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        if grid[x][y] == 'empty':
            grid[x][y] = 'treasure'
            treasures_placed += 1
    
    return grid

def prompt_player_move():
    """
    Prompt the player for their move
    Returns:
        str: player's move direction
    """
    while True:
        try:
            move = input("Enter your move (up, down, left, right): ").strip().lower()
            if move in MOVES:
                return move
            else:
                raise ValueError
        except ValueError:
            print("Invalid move. Please enter up, down, left, or right.")

def update_player_position(player_position, move):
    """
    Calculate new position based on move
    Returns:
        tuple: new (row, col) position
    """
    row, col = player_position
    dr, dc = MOVES[move]
    new_row, new_col = row + dr, col + dc
    
    if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
        return (new_row, new_col)
    else:
        raise IndexError("Cannot move outside the grid!")

def check_for_treasure(grid, player_position, found_treasures):
    """
    Check if current position has treasure
    Returns:
        bool: True if treasure found, False otherwise
    """
    row, col = player_position
    if grid[row][col] == 'treasure':
        grid[row][col] = 'empty'
        found_treasures.append((row, col))
        return True
    return False

def all_treasures_found(grid):
    """
    Check if all treasures have been found
    Returns:
        bool: True if no treasures remain, False otherwise
    """
    for row in grid:
        if 'treasure' in row:
            return False
    return True

def display_grid(player_position, grid, found_treasures):
    """
    Display the grid with player and revealed treasures
    """
    print("\nCurrent Grid:")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) == player_position:
                print("P", end=" ")
            elif (i, j) in found_treasures:
                print("T", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def main():
    """
    Main game loop
    """
    grid, player_position = initialize_game()
    treasures_remaining = NUM_TREASURES
    found_treasures = []

    while True:
        display_grid(player_position, grid, found_treasures)
        print(f"Treasures remaining: {treasures_remaining}")
        print(f"Current position: {player_position}")

        move = prompt_player_move()

        try:
            new_position = update_player_position(player_position, move)
            player_position = new_position

            if check_for_treasure(grid, player_position, found_treasures):
                treasures_remaining -= 1
                print(f"You found a treasure! {treasures_remaining} remaining.\n")

                if all_treasures_found(grid):
                    display_grid(player_position, grid, found_treasures)
                    print("Congratulations! You found all the treasures!")
                    break

        except IndexError as e:
            print(f"Error: {e} Please try again.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

if __name__ == "__main__":
    main()
    print("Thank you for playing the Treasure Hunt Game!")
    print("Goodbye!")