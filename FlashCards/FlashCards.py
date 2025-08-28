# ITSS / OPRE 3311 – Introduction to Programming 
#  Project: FlashCards  
# Student Name: Shreyas Kanagal
# Date Completed: 2/24/2025
 
# Import necessary modules 
import random 
 
# Display intro message
print ("Welcome to the Legendary Math Flashcard Game!")

# Prompt user for their name 
name = input ("Please enter your name: ")
print ("Hello", name, "!")
 
# Start loop for play again 
while True: 
    # Prompt user for the type of math problem
    print ("Enter: A for Addition, S for Subtraction, M for Multiplication, D for Division!")
    type_problem = input ("What type of math problem would you like to solve?")

    # Convert problem type to upper case 
    type_problem= type_problem.upper()

    print ("Pick the range of numbers you want to work with for the problems.")

    # Prompt user for the lowest value for the problem numbers 
    low = int(input ("Enter the lowest value for the problem numbers: "))

     # Prompt user for the highest value for the problem numbers
    high = int(input ("Enter the highest value for the problem numbers: "))

    if low > high:
        print ("Invalid range. Try again.")
        continue

    # Prompt user for the number of problems to work on
    number_of_problems = int(input ("Enter the number of problems you would like to work on. Make it a challenge: "))
 
    # Initialize counters for attempted and correct problems 
    attempted = 0 
    correct = 0 
 
    # Start loop for number of problems 
    for _ in range(number_of_problems): 
        # Generate random factors within the specified range 
        factor1 = random.randint(low, high) 
        factor2 = random.randint(low, high) 
        
        # Create problem based on selected problem type 
        if type_problem == 'A': 
            # Addition problem 
            answer = factor1 + factor2
            user_answer = int(input(f"What is the sum of {factor1} + {factor2}? "))

        elif type_problem == 'S': 
            # Subtraction problem 
            answer = factor1 - factor2
            user_answer = int(input(f"What is the difference of {factor1} - {factor2}? "))

        elif type_problem == 'M': 
            # Multiplication problem 
            answer = factor1 * factor2
            user_answer = int(input(f"What is the product of {factor1} * {factor2}? "))

        elif type_problem == 'D': 
            # Division problem
            while factor2 == 0:
                factor2 = random.randint(low, high) # Ensure divisor is not zero
            answer = round(factor1 / factor2, 2)
            user_answer = float(input(f"What is the quotient of {factor1} / {factor2}? (The answer should be rounded to two decimal places.) "))
        # Check if the provided problem type is valid
        else: 
            print ("Invalid problem type. Please try again.")
            break
    
        # Calculate correct answer 
        if user_answer == answer: 
            print ("Correct!")
            correct += 1 
        else: 
            print ("Incorrect!")

        # Update counters for attempted and correct problems
        attempted += 1

# Display the number of problems attempted, number correct, and percentage correct 
    if attempted > 0:
        percentage_correct = round(correct / attempted * 100, 2)
        print (f"You attempted {attempted} problems and got {correct} correct. You achieved a percentage of {percentage_correct}%!")
           
# Prompt user if they want to play another session 
    play_again = input ("Want another chance at the Legendary Math Flashcard Game? (enter yes/no, the game will end for anything else.): ")
    # If user does not want to play again, break the loop
    if play_again != 'yes':
        break

# Display outro message 
print ("Thank you for playing! I hope you enjoyed yourself,", name, "!")
