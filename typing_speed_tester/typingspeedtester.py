#note: please download the starting json file and put it in the same folder as this code
#"sentence_typing.json"

#importing and initializing
import json
import datetime
import time
import random 
local_highscore = []

#functions
def play_game():

    with open("sentence_typing.json", "r") as the_file:

        #get files biggest number in the dict
        sentence_dict = json.load(the_file)
        number_list = [int(num) for num in sentence_dict.keys()]
        biggest_num = max(number_list)

        #random number with max being files big number to choose a sentence
        chosen_num = random.randint(1, biggest_num)
        chosen_sentence = sentence_dict[str(chosen_num)]

        #start sentence and mark start time with a while loop, if sentence wrong then keep running until right, then when done mark end time and calculate the difference between start and end time
        start_time = time.strftime("%H:%M:%S")
        start_time = datetime.datetime.strptime(start_time, "%H:%M:%S")
        print(f"Type the following sentence as fast as you can!\n\n'{chosen_sentence}'\n\nPress enter when you're done!")
        game_input = input("Your response: ")
        while game_input != chosen_sentence:
            print("Try again! ")
            print(f"Type the following sentence as fast as you can!\n\n'{chosen_sentence}'\n\nPress enter when you're done!")
            game_input = input(f"Your response: ")
        end_time = time.strftime("%H:%M:%S")
        end_time = datetime.datetime.strptime(end_time, "%H:%M:%S")

        #calculating the time it took
        delta = abs((start_time - end_time).total_seconds())

        #final value
        print(f"\nIt took you {int(delta)} seconds to finish typing your sentence!")
        return int(delta)

#main
while True:
    player_check = input("\nWhat do you want to do?\n[P]lay game\n[V]iew highscore\n[C]redits\n[E]nd game\nYour input: ")

    #option to play
    if player_check.lower() == "p":
        score = play_game()
        local_highscore.append(score)

    #option to view highscores locally
    elif player_check.lower() == "v":
        local_highscore.sort()
        count = 1
        print("\n> Highscores for this run <\n")
        for score in local_highscore:
            if count > 5:
                break
            print(f"{count}: {local_highscore[count - 1]}")
            count += 1

    #option to check the credits
    elif player_check.lower() == "c":
        print("\nThis game was developed by Beth!")
        print("Libraries used:\n- JSON\n- DateTime\n- Time\n- Random")

    #option to end game
    elif player_check.lower() == "e":
        end_game_check = input("\nAre you sure you want to end the game?\n[Y]es\n[N]o\nYour choice: ")
        if end_game_check.lower() == "y":
            print("\nThank you for playing!")
            break
        else:
            print("\nYou have chosen to continue playing!")

    #if there is an error in the players input, this runs
    else:
        print("Please input a valid choice!")