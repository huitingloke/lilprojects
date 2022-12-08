import random
import math
import time

monsters = [
    ("Arccot", 5, 1),
    ("Potatoy", 3, 2),
    ("Mooshy Roomy", 2, 1),
    ("Noion", 2, 2),
    ("Gralic", 3, 1)
]

weapons = [
    ("Dagger", 1),
    ("Pistol", 2),
    ("Shuriken", 3)
]

player_x, player_y = 4, 4
health = 10
weapon = weapons[0]
score = 0

def load_map(file):
    final_dict = {}
    with open(file, "r") as the_file:
        y = 0
        for line in the_file:
            line = line.rstrip()
            if line[0] == "-":
                continue
            x = 0
            for ch in line:
                final_dict[(x, y)] = ch
                x += 1
            y += 1
    return final_dict

def view_map(dictionary):
    ref_number = math.sqrt(len(dictionary))
    count = 1
    for key in dictionary:
        if count < 10:
            print(dictionary[key], end="")
            count += 1
        else:
            print(dictionary[key])
            count = 1
    return ""

def move(player_input, player_x, player_y): #spaghet code
    global map_dictionary
    check = False
    previous_x, previous_y = player_x, player_y
    if player_input == "^" and player_y - 1 > 0:
        check = True
        player_y -= 1
    elif player_input == "v" and player_y < math.sqrt(len(map_dictionary)) - 2:
        check = True
        player_y += 1
    elif player_input == "<" and player_x - 1 > 0:
        check = True
        player_x -= 1
    elif player_input == ">" and player_x < math.sqrt(len(map_dictionary)) - 2:
        check = True
        player_x += 1
    if check:
        map_dictionary[(previous_x, previous_y)] = " "

    return map_dictionary[(player_x, player_y)], player_x, player_y

def treasure(health, weapon):
    global score
    lucky_number = random.randint(0, len(monsters) - 1)
    w_name, w_attack = weapon
    e_name, e_health, e_attack = monsters[lucky_number]
    while True:
        e_health -= w_attack
        print(f"You did {w_attack} damage to {e_name}! It has {e_health} health remaining.")
        if e_health <= 0:
            print(f"You won the battle! You have {health} health remaining.")
            break
        health -= e_attack
        if health <= 0:
            print(f"You lost the battle!")
            break
        print(f"{e_name} hurt you for {e_attack} damage! You have {health} health remaining.")
        time.sleep(1)
    old_weapon = weapon
    weapon = weapons[random.randint(0, len(weapons) - 1)]
    if old_weapon == weapon:
        print(f"Your {weapon} remains the same!")
    elif old_weapon[1] < weapon[1]:
        print(f"Your {old_weapon} was upgraded to a {weapon}!")
    elif old_weapon[1] > weapon[1]:
        print(f"Your {old_weapon} was downgraded to a {weapon}! Bad luck~")
    score += 1
    return health, weapon

def fountain(health):
    num_rand = random.randint(1, 5)
    fountain_check = input("Do you want to partake in the fountain of youth? y | n : ")
    fountain_check = fountain_check.lower()
    while fountain_check != "y" and fountain_check != "n":
        print("Please input a valid answer!")
        fountain_check = input("Do you want to partake in the fountain of youth? y | n : ")
        fountain_check = fountain_check.lower()
    if fountain_check == "y":
        if random.randint(1, 2) == 1:
            health += num_rand
            print(f"You earned {num_rand} health!")
            print(f"You now have {health} health!")
        else:
            health -= num_rand
            print(f"You lost {num_rand} health!")
            print(f"You now have {health} health!")
    else:
        print("You chose not to touch the fountain. The fountain is sad.")
    return health

def mine_gameplay(health):
    chosen_one = random.randint(1, 5)
    guess_number = input("Welcome to the mine! Guess the number from 1 to 5! ")
    if int(guess_number) == chosen_one:
        health *= 2
        print(f"You guessed correctly!\nYour health has been doubled! You now have {health} health.")
    else:
        health -= 3
        print(f"You guessed incorrectly!\nYou lost 3 health. Your health is now {health}.")
    return health

#loading the game in
map_number = random.randint(1, 3)
map_name = f"map{map_number}.txt"
map_dictionary = load_map(map_name)

#game loop
while health > 0 and score < 4:
    view_map(map_dictionary)
    player_input = input("What direction will you travel? | ^ v < > : ")
    if player_input in "^v><":
        
        action_square, player_x, player_y = move(player_input, player_x, player_y)
        map_dictionary[(player_x, player_y)] = "O"

        if action_square == " ":
            continue

        elif action_square == "T":
            health, weapon = treasure(health, weapon)

        elif action_square == "M":
            health = mine_gameplay(health)

        elif action_square == "F":
            health = fountain(health)

    else:
        print("Please input a valid move!")

if health <= 0:
    print(f"You died! Thanks for playing~ Your score was {score}.")
elif score > 3:
    print(f"You won! Thank you for playing!")