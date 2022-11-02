#note: skips the 0, 0 cell as it assumes the keys to the dictionary do not need a title
#note: if you would like me to make this a function so you can import it, please let me know~

#imports
import json

#getting user input for the files in the same folder + setting up variables
final_dictionary = {}
print("Note: Ensure the CSV file you want to change into a JSON is in the same folder as this script.")
csv_file = input("CSV input file name: ")
json_file = input("JSON output file name: ")

#splitting up the csv file
with open(csv_file, "r") as the_file:

    header_list = []
    line_count = 1
    for line in the_file:

        #setting up dictionary descriptors for the json file
        if line_count == 1:
            line = line.rstrip()
            col = line.split(",")
            for num in range(len(col)):
                if num != 0:
                    header_list.append(col[num])
            line_count += 1

        #main repeating process to create the dictionary
        elif line_count != 1:
            line = line.rstrip()
            col = line.split(",")
            final_dictionary[col[0]] = {}
            for item in header_list:
                for num in range(len(header_list)): 
                    if header_list[num] == item:
                        final_dictionary[col[0]][item] = col[num + 1]

#writing the json file
final_file = open(json_file, "w")
json.dump(final_dictionary, final_file, indent=6)
final_file.close()

#done!!!
print("Operation complete!")