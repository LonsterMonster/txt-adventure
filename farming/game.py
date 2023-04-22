import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

# Define game variables
player_name = ""
player_location = "home"
crops = []
animals = []
explored_locations = []

# Define game functions
def show_intro():
    print(Fore.GREEN + """
  _____                       _            _   _             
 / ____|                     (_)          | | (_)            
| (___   ___ _ __ __ _ _ __  _ _ __   ___| |_ _  ___  _ __  
 \___ \ / __| '__/ _` | '_ \| | '_ \ / _ \ __| |/ _ \| '_ \ 
 ____) | (__| | | (_| | |_) | | | | |  __/ |_| | (_) | | | |
|_____/ \___|_|  \__,_| .__/|_|_| |_|\___|\__|_|\___/|_| |_|
                      | |                                    
                      |_|                                    
""")

    print(Fore.YELLOW + "Welcome to the text adventure game!\n")

def show_location():
    print(Fore.BLUE + f"\nYou are currently at {player_location}.")

    if player_location == "home":
        print("You are in your cozy little house.")
    elif player_location == "field":
        print("You are standing in your field. You can plant and harvest crops here.")
    elif player_location == "barn":
        print("You are inside your barn. Your animals are here.")
    elif player_location == "forest":
        print("You are in the forest. There are many places to explore here.")
    elif player_location == "river":
        print("You are at the river. You can fish here.")
    elif player_location == "town":
        print("You are in town. There are many shops and people to talk to here.")

def go(direction):
    global player_location

    if direction == "home":
        player_location = "home"
        print("You go back home.")
    elif direction == "field":
        if "field" not in explored_locations:
            print("You've discovered a new location: field!")
            explored_locations.append("field")

        player_location = "field"
       
        print("You go to the field.")
    elif direction == "barn":
        if "barn" not in explored_locations:
            print("You've discovered a new location: barn!")
            explored_locations.append("barn")

        player_location = "barn"
        print("You go to the barn.")
    elif direction == "forest":
        if "forest" not in explored_locations:
            print("You've discovered a new location: forest!")
            explored_locations.append("forest")

        player_location = "forest"
        print("You go to the forest.")
    elif direction == "river":
        if "river" not in explored_locations:
            print("You've discovered a new location: river!")
            explored_locations.append("river")

        player_location = "river"
        print("You go to the river.")
    elif direction == "town":
        if "town" not in explored_locations:
            print("You've discovered a new location: town!")
            explored_locations.append("town")

        player_location = "town"
        print("You go to town.")
    else:
        print(Fore.RED + "Invalid direction. Please choose a valid direction.")

def plant_crop(crop):
    global crops

    if "field" not in explored_locations:
        print(Fore.RED + "You need to find the field first!")
        return

    if crop == "corn":
        print(Fore.GREEN + "You plant a corn seed.")
        crops.append("corn")
    elif crop == "potato":
        print(Fore.GREEN + "You plant a potato seed.")
        crops.append("potato")
    elif crop == "tomato":
        print(Fore.GREEN + "You plant a tomato seed.")
        crops.append("tomato")
    else:
        print(Fore.RED + "Invalid crop. Please choose a valid crop.")

def harvest_crop(crop):
    global crops

    if "field" not in explored_locations:
        print(Fore.RED + "You need to find the field first!")
        return

    if crop in crops:
        print(Fore.GREEN + f"You harvest a {crop}.")

        if random.randint(1, 3) == 1:
            print(Fore.YELLOW + f"You found a rare {crop}!")
    else:
        print(Fore.RED + "Invalid crop. Please choose a valid crop.")

def buy_animal(animal):
    global animals

    if "town" not in explored_locations:
        print(Fore.RED + "You need to find the town first!")
        return

    if animal == "chicken":
        print(Fore.GREEN + "You buy a chicken.")
        animals.append("chicken")
    elif animal == "cow":
        print(Fore.GREEN + "You buy a cow.")
        animals.append("cow")
    elif animal == "pig":
        print(Fore.GREEN + "You buy a pig.")
        animals.append("pig")
    else:
        print(Fore.RED + "Invalid animal. Please choose a valid animal.")

def play_game():
    global player_name

    show_intro()

    while not player_name:
        player_name = input(Fore.YELLOW + "What is your name? ")

    print(Fore.GREEN + f"\nWelcome to the game, {player_name}!")

    while True:
        show_location()

        action = input(Fore.YELLOW + "\nWhat would you like to do? ")

        if action.startswith("go "):
            go(action.split(" ")[1])
        elif action.startswith("plant "):
            plant_crop(action.split(" ")[1])
        elif action.startswith("harvest "):
            harvest_crop(action.split(" ")[1])
        elif action.startswith("buy "):
                        buy_animal(action.split(" ")[1])
        elif action == "inventory":
            print(Fore.YELLOW + "\nInventory:")
            print(Fore.CYAN + f"Crops: {', '.join(crops)}")
            print(Fore.CYAN + f"Animals: {', '.join(animals)}")
        elif action == "quit":
            print(Fore.GREEN + "\nThanks for playing!")
            break
        else:
            print(Fore.RED + "Invalid action. Please choose a valid action.")

if __name__ == "__main__":
    play_game()

