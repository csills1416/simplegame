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
    "dexterity": 5,
    "inventory": []
}

# Game Location for Player
game_state = {
    "player_location": "sewer"
}

def get_ai_response(prompt):
    # Mock AI response for simplicity
    return "I'm just a simple text-based AI."

def move(direction):
    # Example movement function
    if direction == "west":
        print("You can't go further into the sewers.")
    elif direction == "east":
        print("You can't go further into the sewers.")
    else:
        print("You can't go that way.")

def generate_encounter(location):
    # Generate a random encounter with a creature based on location
    if location == "sewer":
        creature_name = random.choice(["giant_rat", "sewer_goblin"])
    creature_stats = creature_data[creature_name]
    return creature_name, creature_stats

def battle(player_stats, creature_stats):
    # Simulated battle, just deduct health for now
    player_damage = random.randint(1, player_stats["strength"])
    creature_damage = random.randint(1, creature_stats["strength"])
    player_stats["hp"] -= creature_damage
    creature_stats["hp"] -= player_damage
    return player_stats, creature_stats

def explore(location):
    if location == "sewer":
        # Generate a random encounter
        creature_name, creature_stats = generate_encounter(location)
        print(f"You encounter a {creature_name}!")
        # Simulated battle
        player_stats, creature_stats = battle(player_stats, creature_stats)
        print(f"You defeated the {creature_name}!")
        # Update player stats and game state
        player_stats["inventory"].append(creature_name)
        if player_stats["hp"] <= 0:
            print("You have been defeated. Game Over.")
            return "game_over"
    return player_stats

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

        # Update game state to prompt the player to explore
        game_state["objective"] = "Leave the sewers and escape the city."

    # Handle player input
    player_input = input("What do you do? ")
    if player_input.lower() == "quit":
        break
    elif player_input.lower() in ["west", "east"]:
        move(player_input.lower())
        game_state["objective"] = "Explore the sewer."
    elif player_input.lower() == "explore":
        result = explore(game_state["player_location"])
