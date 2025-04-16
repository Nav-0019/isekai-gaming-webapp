import random

MONSTERS = ["Slime", "Goblin", "Orc", "Troll", "Stempede of monster", "Dragon", "Demon God"]
POSITIONS = ["Traveller", "Villager", "Village hero", "Noble", "King", "SSS rank adventurer", "Demi-God"]
WEAPONS = ["Wooden sword", "Iron sword", "Steel sword", "Mithril sword", "Excalibur", "Soul sword", "Sword of light"]

def get_status(level):
    return {
        "monster": MONSTERS[level],
        "position": POSITIONS[level],
        "weapon": WEAPONS[level]
    }

def attack(level, guess):
    monster_attack = random.randint(0, 2**level)
    success = (guess == monster_attack)
    return success, monster_attack
