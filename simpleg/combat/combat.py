import random

# Function to simulate a dice roll
def roll_dice(sides=6):
    return random.randint(1, sides)

# Example player and enemy stats
player_stats = {
    "name": "Player",
    "hp": 100,
    "mp": 50,
    "strength": 10,
    "dexterity": 5
}

enemy_stats = {
    "name": "Enemy",
    "hp": 50,
    "mp": 0,
    "strength": 8,
    "dexterity": 3
}

# Function to handle a player's turn
def player_turn(player_stats, enemy_stats):
    print(f"{player_stats['name']}'s turn:")
    print("1. Attack\n2. Cast spell\n3. Use item\n4. Flee")
    choice = input("Choose an action: ")
    if choice == "1":
        attack(player_stats, enemy_stats)
    elif choice == "2":
        cast_spell(player_stats, enemy_stats)
    elif choice == "3":
        use_item(player_stats)
    elif choice == "4":
        flee()

# Function to handle an enemy's turn
def enemy_turn(player_stats, enemy_stats):
    print(f"{enemy_stats['name']}'s turn:")
    # Enemy AI logic goes here
    attack(player_stats, enemy_stats)

# Function to handle an attack
def attack(attacker_stats, target_stats):
    print(f"{attacker_stats['name']} attacks {target_stats['name']}!")
    # Roll a dice to determine if the attack hits
    if roll_dice() <= attacker_stats['dexterity']:
        damage = roll_dice() + attacker_stats['strength']
        print(f"Hit! {damage} damage dealt.")
        target_stats['hp'] -= damage
    else:
        print("Miss!")

# Function to handle casting a spell
def cast_spell(player_stats, enemy_stats):
    if player_stats['mp'] >= 10:  # Assuming spell costs 10 MP
        print(f"{player_stats['name']} casts a spell!")
        # Magic logic goes here
        player_stats['mp'] -= 10
    else:
        print("Not enough MP!")

# Function to handle using an item
def use_item(player_stats):
    print("Item used!")  # Placeholder

# Function to handle fleeing from battle
def flee():
    print("You fled from the battle!")
    # Placeholder for fleeing logic

# Example combat flow
def simulate_combat(player_stats, enemy_stats):
    while player_stats['hp'] > 0 and enemy_stats['hp'] > 0:
        player_turn(player_stats, enemy_stats)
        if enemy_stats['hp'] <= 0:
            print("Enemy defeated!")
            break
        enemy_turn(player_stats, enemy_stats)
        if player_stats['hp'] <= 0:
            print("Player defeated!")
            break

# Example usage
simulate_combat(player_stats, enemy_stats)
