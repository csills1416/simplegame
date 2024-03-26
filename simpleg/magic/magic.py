import random

class Magic:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def cast(self):
        # Implement spell effects here
        pass

class Spellbook:
    def __init__(self):
        self.spells = []

    def add_spell(self, spell):
        self.spells.append(spell)

    def get_spell(self, level):
        # Return a random spell of the given level
        spells_of_level = [spell for spell in self.spells if spell.level == level]
        if not spells_of_level:
            return None
        return random.choice(spells_of_level)

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.spellbook = Spellbook()

    def learn_spell(self, spell):
        self.spellbook.add_spell(spell)

    def cast_spell(self):
        # Get a spell based on the player's level
        spell = self.spellbook.get_spell(self.level)
        if spell:
            print(f"{self.name} casts {spell.name}: {spell.description}")
            spell.cast()
        else:
            print(f"{self.name} does not know any spells of level {self.level}")

# Example spells
fireball = Magic("Fireball", "Launches a fiery projectile")
heal = Magic("Heal", "Restores health to the target")
teleport = Magic("Teleport", "Instantly transports the caster to a designated location")

# Create a spellbook for each class
mage_spellbook = Spellbook()
mage_spellbook.add_spell(fireball)
mage_spellbook.add_spell(heal)

# Create a player character
player = Player("Alice", 1)
player.learn_spell(fireball)
player.learn_spell(heal)

# Example usage
player.cast_spell()
