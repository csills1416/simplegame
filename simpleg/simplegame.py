import json
import random

# Load creature data from creatures.json
with open('creatures.json', 'r') as f:
    creature_data = json.load(f)

# Example player stats
player_stats = {
    "level": 1,
    "xp": 0,
    "hp": 100,
    "strength": 10,
    "dexterity": 5
}

# Game Location for Player
game_state = {
    "player_location": "sewer",
    "inventory": []
}

def get_ai_response(prompt):
    # Mock AI response for simplicity
    return "I'm just a simple text-based AI."

def move(direction):
    # Example movement function
    if direction == "right":
        game_state["player_location"] = "city_streets"
        print("You head towards the city streets.")
    elif direction == "left":
        game_state["player_location"] = "refugees"
        print("You head towards the group of refugees.")
    else:
        print("You can't go that way.")

def generate_encounter():
    # Generate a random encounter with a creature
    creature_name = random.choice(list(creature_data.keys()))
    creature_stats = creature_data[creature_name]
    return creature_name, creature_stats

# Combat system
def initialize_battle(player_party, enemy_party):
    # Initialize battle, set up initial conditions
    pass

def player_turn(player_party, enemy_party):
    # Handle player's turn
    pass

def enemy_turn(player_party, enemy_party):
    # Handle enemy's turn
    pass

def resolve_actions(player_party, enemy_party):
    # Resolve actions, calculate damage, etc.
    pass

# Example friendly NPC
friendly_npc = {
    "name": "Inquisitor Geld",
    "location": "sewer",
    "dialogue": [
        "You see a figure huddled in the corner. As you approach, you recognize the distinctive robes of an Inquisitor.",
        "Inquisitor Geld looks up, his eyes wary. 'Who goes there?' he demands.",
        "You explain your situation, and Inquisitor Geld nods. 'I too seek to escape this madness. Perhaps we can help each other.'"
    ],
    "quest": "Inquisitor Geld asks you to retrieve his confiscated spellbook from the Inquisitorial headquarters."
}

def interact_with_npc(npc):
    for dialogue_line in npc["dialogue"]:
        print(dialogue_line)
    
    if "quest" in npc:
        print("Quest:", npc["quest"])
        accept_quest = input("Do you accept the quest? (yes/no) ")
        if accept_quest.lower() == "yes":
            print("You have accepted the quest.")
            # Perform quest-related actions
        else:
            print("You decline the quest.")

# Main game loop
while True:
    # Introductory section
    if game_state["player_location"] == "sewer":
        print("You wake up, groggy, a sharp pain on the back of your head. The night before is a complete blur.")
        print("In front of you is a campfire, its flames roaring and being stoked by a cloaked stranger sitting behind the fire.")
        print("The stranger's face is hidden behind a hood. He's poking the wood on the fire with a rusty sword, making sure it doesn't go out.")
        print("The stranger notices you are awake. He places the rusty sword by his side and looks at you.")
        print("Stranger: You're awake. For a second there I thought that Maji had scrambled your brains. Can you speak? Did he scramble that noggin' of yours?")

        # Use mock AI to generate response
        ai_response = get_ai_response("The stranger asks if you know what's happened in the city.")
        print("Stranger:", ai_response)

        # Explain the objective
        print("Stranger: Well, let me fill you in. The city's in chaos. The Black Rose Society struck hard, and now it's every man for himself.")
        print("Stranger: You look lost, friend. If you're smart, you'll head west. Maybe my old comrades managed to escape. As for me, I'm done with this city.")

        # Update game state to prompt the player to explore
        game_state["objective"] = "Leave the sewers and escape the city."

    # Handle player input
    player_input = input("What do you do? ")
    if player_input.lower() == "quit":
        break
    elif player_input.lower() in ["right", "left"]:
        move(player_input.lower())
    elif player_input.lower() == "explore":
        # Check if the player has achieved the objective
        if "objective" in game_state and game_state["player_location"] != "sewer":
            print("You successfully escaped the city. Congratulations!")
            break
        else:
            print("You can't do that right now.")
    elif player_input.lower() == "talk":
        # Interact with the friendly NPC
        if game_state["player_location"] == friendly_npc["location"]:
            interact_with_npc(friendly_npc)
        else:
            print("There is no one to talk to here.")
    else:
        print("You can't do that right now.")


