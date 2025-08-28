import random
import re
import os

# ===== FILE HANDLING FUNCTIONS =====
def read_words(file_name):
    """Reads words from input.txt and returns a list. Handles errors."""
    try:
        with open(file_name, 'r') as file:
            content = file.read().strip()
            words = re.findall(r'\b\w+\b', content)  # Extract words using regex
            if not words:
                print("Error: No words found in the file.")
                return None
            return words
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found. Please ensure it exists.")
        return None

def write_results(file_name, results):
    """Writes results to output.txt."""
    try:
        with open(file_name, 'w') as file:
            file.write(results)
        print(f"Results saved to '{file_name}'.")
    except IOError:
        print(f"Error: Could not write to '{file_name}'. Check permissions.")

# ===== GRID GENERATION FUNCTIONS =====
def generate_grid(words, size=10):
    """Generates a word search grid with random word placements."""
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    for word in words:
        word = word.upper()
        placed = False
        attempts = 0
        max_attempts = 100
        while not placed and attempts < max_attempts:
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                row = random.randint(0, size - 1)
                col = random.randint(0, size - len(word))
                if all(grid[row][col + i] in [' ', word[i]] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row][col + i] = word[i]
                    placed = True
            else:  # Vertical
                row = random.randint(0, size - len(word))
                col = random.randint(0, size - 1)
                if all(grid[row + i][col] in [' ', word[i]] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row + i][col] = word[i]
                    placed = True
            attempts += 1
    # Fill empty spaces with random letters
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = chr(random.randint(65, 90))
    return grid

def print_grid(grid):
    """Prints the grid with borders and indices."""
    size = len(grid)
    print("\n   " + "".join([str(i).rjust(2) for i in range(size)]))
    print("  +" + "---" * size + "+")
    for i, row in enumerate(grid):
        print(f"{i} | " + " ".join(row) + " |")
    print("  +" + "---" * size + "+")

# ===== WORD SEARCH LOGIC =====
def find_word(grid, word):
    """Returns coordinates of a word in the grid (if found)."""
    word = word.upper()
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if grid[row][col] == word[0]:
                # Check horizontal
                if col + len(word) <= size and all(grid[row][col + i] == word[i] for i in range(len(word))):
                    return [(row, col + i) for i in range(len(word))]
                # Check vertical
                if row + len(word) <= size and all(grid[row + i][col] == word[i] for i in range(len(word))):
                    return [(row + i, col) for i in range(len(word))]
    return []

def interact_and_locate_words(grid, words):
    """Handles user interaction for word guessing."""
    found_words = []
    for word in words:
        word = word.upper()
        print(f"\nFind the word: {word}")
        print_grid(grid)
        while True:
            user_input = input("Enter all of the coordinates. e.g 5, 1 5, 2 ...").strip()
            if re.fullmatch(r'(\d+,\d+\s)+\d+,\d+', user_input):
                coordinates = [tuple(map(int, coord.split(','))) for coord in user_input.split()]
                break
            else:
                print("Invalid format. Use 'row,col' pairs like '1,2 1,5'.")
        actual_coordinates = find_word(grid, word)
        if coordinates == actual_coordinates:
            found_words.append(word)
            print(f"Correct! '{word}' is at {coordinates}.")
            for (row, col) in coordinates:
                grid[row][col] = grid[row][col].lower()  # Highlight
        else:
            print(f"Wrong. Correct coordinates for '{word}': {actual_coordinates}.")
    return found_words

# ===== MAIN FUNCTION =====
def main():
    print("=== WORD SEARCH PUZZLE GAME ===")
    
    # File names (update these if needed)
    input_file = input("Place your words in an input file of your creation (one line, separated by commas/spaces). Enter the path to your input file here:")
    output_file = "output.txt"
    
    # Read words
    words = read_words(input_file)
    if not words:
        return
    
    # Generate grid
    grid = generate_grid(words)
    print("\nGenerated Word Search Grid:")
    print_grid(grid)
    
    # User interaction
    found_words = interact_and_locate_words(grid, words)
    
    # Save results
    results = f"Found {len(found_words)}/{len(words)} words:\n" + "\n".join(found_words)
    write_results(output_file, results)

if __name__ == "__main__":
    main()