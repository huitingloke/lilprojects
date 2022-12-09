import random

credit = 100
roll_price = 5
inventory = []
unlocked = 5
unlock_price = 50

with open("storage.txt", "r") as the_file:
    plushies = []
    for line in the_file:
        line = line.rstrip()
        col = line.split(",")
        plushies.append((col[0], col[1]))

#gacha stuff
def roll(credit, inventory, storage, roll_num):
    global unlocked
    credit -= (roll_price * roll_num)
    for num in range(roll_num):
        plush = random.randint(0, unlocked - 1)
        inventory.append(storage[plush])
        print(f"You rolled {storage[plush][0]}! Rarity: {storage[plush][1]}")
    return credit, inventory, storage

def guess_the_plushies(credit):
    print("""
------------------ GUESS ------------------
 Every plushie is represented by an X! If
 you guess closely enough to the number of
            plushies, you win!
-------------------------------------------
    """)
    plushie_count = random.randint(1, 100)
    for number in range(plushie_count):
        print("X", end="")
    guess = input("\nHow many plushies are there? ")
    try:
        guess = int(guess)
        if plushie_count == guess:
            credit += 35
            print(f"You got it right! You earned 35 credits! You now have {credit} credits.")
            return credit
        elif abs(plushie_count - guess) <= 5:
            credit += 10
            print(f"You were close! The number is {plushie_count}.")
            print(f"You earned 10 credits! You now have {credit} credits.")
            return credit
        else:
            print(f"Not even close! You guessed {guess}. There were {plushie_count} plushies!")
    except:
        print("Please input a valid number!")
        return credit

def talk_to_plushies(credit):
    sentence_list = []
    with open("sentences.txt", "r") as the_file:
        for line in the_file:
            line = line.rstrip()
            sentence_list.append(line)
    print("""
------------------ TALK -------------------
 Type the sentence exactly as the plushie
          says it to win credits!
-------------------------------------------
    """)
    num = random.randint(0, len(sentence_list) - 1)
    sentence = sentence_list[num]
    user_input = input(f"Type the sentence exactly as you see it!\n{sentence}\nYour answer: ")
    while user_input != sentence:
        print("Try again!")
        user_input = input(f"Type the sentence exactly as you see it!\n{sentence}\nYour answer: ")
    credit += 10
    print(f"Correct! You have earned 10 credits!\nYou have {credit} credits.")
    return credit

def rock_paper_scissors(credit):
    rps_list = ["r", "p", "s"]
    rps_dict = {"r": "Rock", "p": "Paper", "s": "Scissors"}
    print(f"""
----------- ROCK PAPER SCISSORS -----------
   Play rock, paper, scissors against the 
     plushie and stand to win credits!
-------------------------------------------
    """)
    while True:
        com_choice = random.choice(rps_list)
        print("\nType 'r' for rock, 'p' for paper, and 's' for scissors!")
        print("Or type 'q' to quit.")
        user_choice = input("What would you like to play? ")
        if user_choice.lower() == "r":
            if com_choice == "r":
                print(f"Tie! The plushie chose {rps_dict[com_choice]}!")
                credit += 5
                print(f"You earned 5 credits! You have {credit} credits.")
            elif com_choice == "p":
                print(f"You lost! The plushie chose {rps_dict[com_choice]}!")
                print(f"You didn't earn any credits. You have {credit} credits.")
            else:
                print(f"You won! The plushie chose {rps_dict[com_choice]}!")
                credit += 15
                print(f"You earned 15 credits! You have {credit} credits.")
        elif user_choice.lower() == "p":
            if com_choice == "r":
                print(f"You won! The plushie chose {rps_dict[com_choice]}!")
                credit += 15
                print(f"You earned 15 credits! You have {credit} credits.")
            elif com_choice == "p":
                print(f"Tie! The plushie chose {rps_dict[com_choice]}!")
                credit += 5
                print(f"You earned 5 credits! You have {credit} credits.")
            else:
                print(f"You lost! The plushie chose {rps_dict[com_choice]}!")
                print(f"You didn't earn any credits. You have {credit} credits.")
        elif user_choice.lower() == "s":
            if com_choice == "r":
                print(f"You lost! The plushie chose {rps_dict[com_choice]}!")
                print(f"You didn't earn any credits. You have {credit} credits.")
            elif com_choice == "p":
                print(f"You won! The plushie chose {rps_dict[com_choice]}!")
                credit += 15
                print(f"You earned 15 credits! You have {credit} credits.")
            else:
                print(f"Tie! The plushie chose {rps_dict[com_choice]}!")
                credit += 5
                print(f"You earned 5 credits! You have {credit} credits.")
        elif user_choice.lower() == "q":
            print("Returning to the main menu!")
            break
        else:
            print("Please input a valid option!")
    return credit

def earn(credit):
    while True:
        print("""
------------------ EARN -------------------
[G]uess the plushies
[T]alk to plushies
[R]ock paper scissors
[Q]uit
-------------------------------------------
        """)
        job_check = input("Which job would you like to do? ")

        if job_check.lower() == "g":
            credit = guess_the_plushies(credit)

        elif job_check.lower() == "t":
            credit = talk_to_plushies(credit)

        elif job_check.lower() == "r":
            credit = rock_paper_scissors(credit)

        elif job_check.lower() == "q":
            print("Returning to the main menu!")
            return credit

        else:
            print("Please enter a valid choice!")

#purchase the chance to gacha better stuff
def buy(credit):
    global unlocked
    global unlock_price
    while True:
        print(f"""
------------------- BUY -------------------
Purchase the chance to gacha more plushies!
You can afford {credit // unlock_price} plushies.
[B]uy
[Q]uit
-------------------------------------------        
        """)
        user_check = input("What would you like to do? ")
        if user_check.lower() == "b":
            num = input("How many plushies do you want to buy? ")
            try:
                num = int(num)
                if num > credit // unlock_price:
                    print("You cannot afford that!")
                    continue
                credit -= num * unlock_price
                for i in range(num):
                    unlocked += 1
                print(f"You have unlocked {num} new plushies!")
                
            except:
                print("Please input a valid number!")

        elif user_check.lower() == "q":
            print("Returning to the main menu...")
            break
        else:
            print("Please make a valid choice!")

    return credit

#purchase the chance to gacha better stuff
def view(inventory):
    for x in range(0, len(inventory)):
        print(f"{x + 1}. {inventory[x][1]}: {inventory[x][0]}")

print("""
--------------- HAPPY GACHA ---------------
 Welcome to Happy Gacha! Here you can grab
      as many prizes as you want!
-------------------------------------------
""")

while True:

    print(f"""
--------------- HAPPY GACHA ---------------
[R]oll -- Get more plushies!
[E]arn -- Get more money!
[B]uy -- Purchase gacha chances!
[V]iew -- See your plushies!
[Q]uit -- Quit the game!
-------------------------------------------
    """)
    player_input = input("Your choice: ")

    if player_input.lower() == "r":
        print(f"""
------------------ ROLL -------------------
You have {credit} credits
You can afford to roll {credit / roll_price} times.
-------------------------------------------
    """)
        roll_num = input("Number of times you want to roll: ")
        try: 
            roll_num = int(roll_num)
            if roll_num > (int(credit // roll_price)):
                print(f"You don't have enough credit to gacha!\nYour credit: {credit}")
                continue
            credit, inventory, plushies = roll(credit, inventory, plushies, roll_num)
        except:
            print("That is not a valid number!")

    elif player_input.lower() == "e":
        credit = earn(credit)
        
    elif player_input.lower() == "b":
        credit = buy(credit)

    elif player_input.lower() == "v":
        view(inventory)
       
    elif player_input.lower() == "q":
        final_check = input("""
--------------- HAPPY GACHA ---------------
    Do you really want to quit? y / n
-------------------------------------------
Your input: """)
        if final_check.lower() == "y":
            break
        
    else:
        print("Please input a valid choice!")

print("""
--------------- HAPPY GACHA ---------------
   Thanks for playing! Hope you had fun!
-------------------------------------------
""")