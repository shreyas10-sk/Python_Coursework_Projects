# Final Project for ITSS/OPRE 3311
# Author: Shreyas Kanagal
# Date: 5/2/2025
# Description: This program simulates a text adventure game where the player makes choices to navigate through a story with multiple paths and endings.

def get_name():
    """
    Get the player's name.
    """
    try:
        name = input("Enter your name, traveler: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        if name.isdigit():
            raise ValueError("Name cannot be a number.")
        return name
    except ValueError as e:
        print(f"Error: {e} Please try again.")
        return get_name()

def print_welcome_message(name):
    """
    Print a welcome message to the player.
    """
    print(f"\nWelcome, {name}, to the Land of Winterstone!")
    print("Rules of the game:")
    print("You will make choices by entering the corresponding number.")
    print("In this land, you will face many challenges and make choices that will determine your fate.")
    print("Choose wisely, for your decisions will shape the story ahead.")
    input("Press Enter to begin your legendary joruney...")
    print("\n")

def get_story(path):
    """
    Get the story based on the chosen path.
    """
    stories = {
        "start": "You awaken in the town of Winterstone, a remote province in the land of Summerfell, with no recollection of your past. As you gather your bearings, a hooded messenger approaches, their voice laced with urgency. They reveal that an ancient prophecy has foretold your arrival—marking you as the one who will shape the fate of the land.",
        "1": "The messenger explains that the land has been invaded by the Demon Kind, and the Queen has requested your presence in the court as the harbinger of the prophecy.",
        "1a": "You stand before the Queen, her eyes filled with desperation and resolve. She beseeches you to take command of the kingdom's army and lead the charge against the Demon Kind. With a heavy heart, she warns that time is running out—Winterstone will not withstand the onslaught much longer.",
        "1a1": "Trained by a seasoned general in the art of war, you lead an army to the land of demons, determined to put an end to the growing threat. With the aid of hired mercenaries, you fight a terrifying battle, ultimately securing victory and saving Summerfell.",
        "1a2": "You leave the land of Summerfell forever, leading to the land's ruin as the Demon Kind overruns the kingdom.",
        "1b": "You uncover the ancient prophecy that binds you to Summerfell's fate—a grim revelation that foretells the kingdom's impending destruction. As the words unfold before you, the weight of destiny settles upon your shoulders.",
        "1b1": "You study the prophecy further, learning more and arming yourself with the knowledge necessary to beat the demons.",
        "1b2": "The magical artifact you stole turns out to be sinister, summoning an ancient force that destroys the land of Summerfell, leaving it in ruin.",
        "2": "You avoid listening to the messenger and abandon the city to avoid the risk of involvement.",
        "2a": "The bandits meet you with uncertainty, believing that you are unworthy of their company. They task you with a trial, threatening death if not completed.",
        "2a1": "Over time, you sharpen your skills, gaining a reputation as a ruthless outlaw. Rising through the ranks, you seize control and become the Bandit King, ruling over the remnants of a shattered world.",
        "2a2": "You narrowly escape the bandits' clutches. You wander alone, until you come across a mercenary camp, where you are offered a chance to join their ranks.",
        "2b": "The mercenaries offer to train you, but you must join them on a dangerous mission that may cost your life.",
        "2b1": "The mission leads you to join the army with your mercenaries to fight the Demon Kind, leading them to destroy the opposition.",
        "2b2": "You leave the land of Summerfell forever, leading to the land falling into ruin.",
    }
    return stories.get(path, "The path ahead is unclear...")

def get_choices(path):
    """
    Returns the available choices for the current path.
    """
    choices = {
        "start": [
            ("Investigate the claims", "1"),
            ("Flee the responsibility by leaving the village", "2")
        ],
        "1": [
            ("Visit the court and meet with the Queen", "1a"),
            ("Sneak into the forbidden library", "1b")
        ],
        "1a": [
            ("Agree to serve the kingdom, taking over the army", "1a1"),
            ("Refuse the Queen's orders, and leave the court", "1a2")
        ],
        "1b": [
            ("Study the prophecy further", "1b1"),
            ("Steal a magical artifact and flee the city", "1b2")
        ],
        "1b1": [
            ("Visit the Court to meet with the Queen, armed with knowledge", "1a"),
            ("Abandon your mission, terrified of the prophecy", "1a2")
        ],
        "2": [
            ("Undertake the Path of the Bandit", "2a"),
            ("Head to the mercenary camp", "2b")
        ],
        "2a": [
            ("Raid a nearby caravan and pass the test", "2a1"),
            ("Refuse the trial, and narrowly escape", "2a2")
        ],
        "2a2": [
            ("Join the mercenary camp", "2b"),
            ("Decline, and choose to live as a wanderer", "2b2")
        ],
        "2b": [
            ("Accept the mission, and train hard", "2b1"),
            ("Decline, and choose to live as a wanderer", "2b2")
        ],
        # Endings don't have further choices
        "1a1": [], "1a2": [], "1b2": [], "2a1": [], "2b1": [], "2b2": []
    }
    return choices.get(path, [])

def print_end_message(name, ending):
    """
    Prints the end message based on the ending achieved.
    """
    endings = {
        "1a1": "Your bravery earns you recognition across the kingdom. Your story is told for generations, remembered as the hero who brought peace in a time of darkness.",
        "1a2": "Summerfell falls to the Demon Kind. Your name is forgotten, lost to history as just another who abandoned their duty.",
        "1b2": "The artifact's power consumes you and destroys Summerfell. Your name becomes synonymous with doom.",
        "2a1": "As demons lay waste to the land, you thrive in the chaos, taking what remains and bending survivors to your will, carving out your own kingdom in the ashes of civilization.",
        "2b1": "Your mercenary band becomes legendary for their stand against the Demon Kind, though at great personal cost.",
        "2b2": "You leave Summerfell to its fate, but find no peace in your wandering, haunted by what might have been."
    }
    
    print("\n" + "="*50)
    print("THE END")
    print("="*50)
    print(endings.get(ending, "Your journey ends here..."))
    print("\n\n\"Nothing is more difficult, and therefore more precious, than to be able to decide.\" - Napoleon Bonaparte")
    print("="*50)

def make_choice(current_path):
    """
    Presents choices based on the current path and returns the next path.
    """
    choices = get_choices(current_path)
    
    if not choices:  # This is an ending
        return None
    
    print("\n" + get_story(current_path))
    print("\nWhat do you do?")
    
    for i, (text, path) in enumerate(choices, 1):
        print(f"{i}. {text}")
    
    while True:
        try:
            choice = input("Enter your choice (number): ").strip()
            if not choice.isdigit():
                raise ValueError
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(choices):
                return choices[choice_index][1]
            raise ValueError
        except ValueError:
            print(f"Please enter a number between 1 and {len(choices)}")

def play_again():
    """
    Prompts for and returns True if the player chooses to play again.
    """
    while True:
        response = input("\nWould you like to play again? (Y/N): ").upper()
        if response in ("Y", "N"):
            return response == "Y"
        print("Please enter Y or N.")

def main():
    # Get the user's name
    name = get_name()
    
    # Print the welcome message and rules
    print_welcome_message(name)
    
    # Main game loop
    while True:
        current_path = "start"
        
        # Game session loop
        while current_path:
            next_path = make_choice(current_path)
            if next_path is None:  # Reached an ending
                print_end_message(name, current_path)
                break
            current_path = next_path
        
        # Check if the user wants to play again
        if not play_again():
            print(f"\nYour journey ends here, {name}. Stay true to your path.")
            break

if __name__ == "__main__":
    main()
