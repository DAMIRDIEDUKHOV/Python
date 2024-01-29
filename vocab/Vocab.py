import random
from words import word_list

lists = word_list
yes_list = []
no_list = []
correct_count = 0
incorrect_count = 0

random.shuffle(lists)  # Shuffling the word list

for word in lists:
    print("Do you know this word?")
    print(word)
    user_input = input()

    if user_input.lower() == "stop":
        break

    if user_input.lower() == "yes":
        yes_list.append(word)
        correct_count += 1
    elif user_input.lower == "no":
        no_list.append(word)
        incorrect_count += 1
    else:
        print("Please enter 'yes' or 'no'.")

print("\n")
print(f"Words you know: {correct_count}")
for known_word in yes_list:
    print(known_word)

print("\n")
print(f"Words you don't know: {incorrect_count}")
for unknown_word in no_list:
    print(unknown_word)


