import random


def show_welcome():
    print("⚔️  Welcome to the Monster Battle Arena! ⚔️")
    print("you are a brave warrior facing the trials of the world!")
    print("--------------------------------------------")

    

def attack(attacker, damage):
    print(f"{attacker} lunges forward and deals {damage} damage!")

def calculate_damage(base_damage):

    if random.random() < 0.20:
        print("CRITICAL STRIKE!")
        return base_damage * 2  
    return base_damage



def take_damage(current_health, damage_taken):
    new_health = current_health - damage_taken
    if new_health < 0:
        new_health = 0
    print(f"Remaining Health:{new_health}\n")
    
    
    return new_health

def heal(current_health, max_health=100):
    heal_amount = random.randint(10, 40)
    current_health=min(current_health+heal_amount, max_health)
    print(f"💚 You used a potion and recovered 20 HP!")
    print(f"Remaining Health: {current_health}\n")
    return current_health
    
show_welcome()

player_health=100
monster_health=100
is_blocking=False
turn_count=1


while monster_health > 0:
    print(f"\n--- TURN {turn_count} ---")
    print("What will you do?")
    print("1. Attack")
    print("2. Heal")
    print("3. Block")
    choice = input("Choose 1 or 2 or 3:")

    if choice == "1":
        damage = calculate_damage(20)
        attack("warrior", damage)
        monster_health = take_damage(monster_health, damage)
    elif choice == "2":
        player_health = heal(player_health)
    elif choice == "3":
        print("The player has raised their shield in defiance!")
        is_blocking = True

    if monster_health <= 0:
        break

    monster_damage = calculate_damage(15)
    if is_blocking == True:
        print("The shield absorbed half of the damage!")
        monster_damage = monster_damage // 2

    attack("Monster", monster_damage)
    player_health = take_damage(player_health, monster_damage)
    is_blocking = False
    turn_count += 1

    if player_health <= 0:
        break
    
if player_health<=0:
    print("Game over you have been defeated!")
else: print("Well done you have Won!"),print("The monster has been slain!")



