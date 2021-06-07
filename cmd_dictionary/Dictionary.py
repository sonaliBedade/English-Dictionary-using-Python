import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print('Did you mean {} instead ?'.format(get_close_matches(word, data.keys())[0]))
        user = input("Press y for yes and n for no ")
        if user == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif user == "n":
            return ("No matches")
        else:
            return ("Wrong input. Enter y or n")
    else:
        return ("No matches")

user = input("Enter \"Y\" to start or \"Q\" to quit: ")
while user == "Y" or user == "y":
    word = input("Enter the word you want to search: ")
    output = meaning(word)
    if type(output) == list:
        for item in output:
            print(" - "+item)
    else:
        print(output)
if user == 'q' or user == 'Q':
    pass
