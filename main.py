# Import for later
import random

# Starting attributes
player_health = 50
player_gold = 0
player_attack = 5
player_defense = 5
playing = False
questing = False

# Functions
def use_sword():
    """Increases player attack power."""
    attack_bonus = 10  # Extra damage dealt
    print(f"You equip the sword. Your attack power increases by {attack_bonus}!")
    return attack_bonus

def use_healing_potion():
    """Restores player health."""
    global player_health
    potion_healing = 15  # Health restored
    max_health = 100  # Max player health
    player_health = min(player_health + potion_healing, max_health)  # Cap at max health
    print(f"You drink a healing potion! Your health is now {player_health}/{max_health}.")

def use_shield():
    """Increases player defense."""
    defense_bonus = 5  # Damage reduction
    print(f"You raise your shield, gaining {defense_bonus} additional defense!")
    return defense_bonus

def add_gold(amount):
    """Adds gold to the player's inventory."""
    global player_gold
    player_gold += amount
    print(f"You collected {amount} gold! You now have {player_gold} gold.")

def rest():
    """Allows the player to rest and regain health."""
    global player_health
    rest_healing = 20
    max_health = 100
    if player_health < max_health:
        player_health = min(player_health + rest_healing, max_health)
        print(f"You take a rest and recover {rest_healing} health.")
        print(f"Your health is now {player_health}/{max_health}.")
    else:
        print("You are already at full health.")

    # Random chance for a wild enemy to ambush the player while resting
    if random.randint(1, 4) == 1:  # 25% chance
        print("While resting, a wild enemy ambushes you!")
        combat()

def combat():
    """Handles a basic enemy combat encounter."""
    global player_health  # Access the player's health
    enemy_health = random.randint(5, 30)  # Random enemy health
    enemy_attack = random.randint(5, 10)  # Enemy attack damage

    in_combat = True
    while in_combat:
        print(f"\nYour Health: {player_health}")
        print(f"Enemy's Health: {enemy_health}")
        print("What will you do?")
        print("1. Attack")
        print("2. Use a healing potion")
        print("3. Run away")

        action = input("> ").strip()
        if action == "1":  # Player attacks
            print("You attack the enemy!")
            enemy_health -= player_attack
            if enemy_health <= 0:
                print("You defeated the enemy!")
                in_combat = False
        elif action == "2":  # Use healing potion
            use_healing_potion()
        elif action == "3":  # Run away
            print("You flee from the fight!")
            in_combat = False
        else:
            print("Invalid action! Please try again.")

        # Enemy attacks if still alive
        if enemy_health > 0:
            print("The enemy attacks you!")
            player_health -= enemy_attack
            print(f"The enemy deals {enemy_attack} damage.")
            if player_health <= 0:
                print("You were defeated by the enemy!")
                in_combat = False

# Main Game Start
print("Text-Based Adventure Game")
print("Type 'y' to play")
user_input = input()
if user_input.lower() == "y":
    print("The game has started!")
    print(f"Player health: {player_health}")
    playing = True
else:
    print("Maybe next time!")

# Main gameplay loop
while playing:
    if player_health <= 0:
        playing = False
        print("You died!")

    print("\nYou are in a village when a stranger approaches and asks if you want to take a dangerous quest.")
    print("Type 'y' to accept, or 'n' to decline.")
    choice = input()
    if choice.lower() == "y":
        print("You chose to continue on the quest, despite the alleged perils.")
        print("The stranger tells you that a treasure chest of his was stolen by a troll. He tells you to retrieve it.")
        print("The stranger gives you a sword, 3 healing potions, a shield, and 250 gold to aid you on your quest.")

        # Update player attributes
        player_attack += use_sword()
        player_defense += use_shield()
        add_gold(250)

        questing = True  # Start the questing loop
        quest_iteration_count = 0  # Tracks how many times the questing loop repeats

        while questing:
            quest_iteration_count += 1

            # Check if the player has reached the troll
            if quest_iteration_count == 3:
                print("\nYou finally reach the troll's cave!")
                print("The massive troll guards its treasure, growling menacingly.")
                print("Prepare for the ultimate fight!")
                troll_health = random.randint(35, 70)
                troll_attack = random.randint(10, 15)
                in_final_fight = True

                while in_final_fight:
                    print(f"\nYour Health: {player_health}")
                    print(f"Troll's Health: {troll_health}")
                    print("What will you do?")
                    print("1. Attack")
                    print("2. Use a healing potion")
                    print("3. Run away (not recommended!)")

                    action = input("> ").strip()
                    if action == "1":
                        print("You swing your sword at the troll!")
                        troll_health -= player_attack
                        if troll_health <= 0:
                            print("You have defeated the troll! You take its treasure back to the village. Upon seeing you, the stranger from before's face lights up. He thanks you profusely and give you a large sum of money from the chest of loot.")
                            in_final_fight = False
                            questing = False
                            playing = False
                    elif action == "2":
                        use_healing_potion()
                    elif action == "3":
                        print("You flee from the troll, abandoning the quest. You think about the stranger, and how dismayed he will be if you didn't return.")
                        in_final_fight = False
                        questing = False
                        playing = False
                    else:
                        print("Invalid action! Try again.")

                    # Troll attacks if still alive
                    if troll_health > 0:
                        print("The troll swings its massive club at you!")
                        player_health -= troll_attack
                        print(f"The troll deals {troll_attack} damage.")
                        if player_health <= 0:
                            print("The troll has defeated you!")
                            in_final_fight = False
                            questing = False
                            playing = False

            else:
                # Regular questing options
                print("\nYou continue on your journey. What will you do?")
                print("1. Continue forward")
                print("2. Check your inventory")
                print("3. Rest")
                print("4. Quit the quest")

                action = input("> ").strip()
                if action == "1":
                    combat()
                    if player_health <= 0:
                        questing = False
                        playing = False
                elif action == "2":
                    print("\nInventory:")
                    print(f"Health: {player_health}, Gold: {player_gold}, Attack: {player_attack}, Defense: {player_defense}")
                    print("Potions: 3 (Example: you can track potions programmatically)")
                elif action == "3":
                    rest()
                elif action == "4":
                    print("You decided to quit the quest and return to the village.")
                    questing = False
                    playing = False
                else:
                    print("Invalid action. Please try again.")

    elif choice.lower() == "n":
        playing = False
        print("Game over. You declined the quest and lived a quiet life.")
    else:
        print("The stranger doesn't understand your response. Please try again.")
