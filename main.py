import random

# Rooms in the game
rooms = {
    "start": {
        "description": "You find yourself in a dark forest.",
        "exits": {"north": "clearing", "west": "cave", "south": "river"},
    },
    "clearing": {
        "description": "You are in a peaceful clearing.",
        "exits": {"south": "start"},
    },
    "cave": {
        "description": "You enter a spooky cave.",
        "exits": {"east": "start", "north": "treasure"},
    },
    "river": {
        "description": "You reach a wide river with a boat.",
        "exits": {"north": "start", "east": "treasure"},
    },
    "treasure": {
        "description": "You found the treasure room!",
        "exits": {},
    },
}

# Actions available in the game
actions = {
    "look": "Look around for more details.",
    "quit": "Quit the game.",
    "inventory": "Check your inventory.",
    "help": "Show available actions.",
}

# Inventory
inventory = []

# Game logic
def play_game():
    current_room = "start"

    print("Welcome to the Adventure Game!\n")
    print(rooms[current_room]["description"])

    while True:
        print("\nWhat would you like to do? (type 'help' for available actions)")
        action = input("> ")

        if action.lower() == "quit":
            print("Thanks for playing!")
            break
        elif action.lower() == "look":
            print(rooms[current_room]["description"])

            if current_room == "cave" and "key" not in inventory:
                print("You notice a shiny key on the ground.")
        elif action.lower() == "inventory":
            print("You have:", ", ".join(inventory))
        elif action.lower() == "help":
            print("Available actions:")
            for key, value in actions.items():
                print(f"{key}: {value}")
        else:
            if current_room == "start":
                if action.lower() in rooms[current_room]["exits"]:
                    current_room = rooms[current_room]["exits"][action.lower()]
                    print(rooms[current_room]["description"])
                else:
                    print("You can't go that way!")
            elif current_room == "cave":
                if action.lower() == "look" and "key" not in inventory:
                    print("You pick up the shiny key from the ground.")
                    inventory.append("key")
                elif action.lower() in rooms[current_room]["exits"]:
                    current_room = rooms[current_room]["exits"][action.lower()]
                    print(rooms[current_room]["description"])
                else:
                    print("You can't go that way!")
            elif current_room == "river":
                if action.lower() in rooms[current_room]["exits"]:
                    if "key" in inventory:
                        print("Congratulations! You unlocked the treasure room and won the game!")
                        break
                    else:
                        print("The door is locked! You need a key to access the treasure.")
                else:
                    print("You can't go that way!")
            else:
                print("Invalid action. Type 'help' for available actions.")

# Start the game
play_game()
