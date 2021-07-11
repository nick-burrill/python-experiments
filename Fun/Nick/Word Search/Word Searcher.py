# 2d array of characters. gunna use numpy
# To find a word:
# Find its first letter
# check what direction it fits in
# check if it has the rest of the letters in that same direction
# if not then go to next instance of first letter

# our file format will simply be a .txt that is human readable
# we will have a comma seperated word list
# 3 newlines
# our wordsearch rows seperated with newline characters

# Possibly remove characters detected to hack in overlap detection

# isAround(row, col, word, array):
    # Check for the 2nd letter in the 8 slots around the first word

from rich import print
import numpy as np


def translate(row, col, direction, distance, array):
    if direction == "left":
        col = col + distance
    elif direction == "right":
        col = col - distance
    elif direction == "up":
        row = row - distance
    elif direction == "down":
        row = row + distance
    elif direction == "up+left":
        row = row - distance
        col = col + distance

    if row > array.shape[0] or col > array.shape[1] or row < 0 or col < 0:
        print("Out of bounds buddy!")

    return array[row][col]


def findWord(array, row, column, word):
    found = False
    start = array[row][column]
    if start != word[0]:
        print("What the fuck. Something before this is broken")
    # First lets store the possible outcomes in a dictionary so we can come back
    possible = {
        "up": True,
        "down": True,
        "left": True,
        "right": True,
        "up+left": True,
        # "up+right": True,
        # "down+left": True,
        # "down+right": True,
    }

    # Next we do a pre-check, eliminate any out of bounds options
    if row + 1 - len(word) < 0:
        possible["up"] = False

    if row + len(word) > array.shape[0]:
        possible["down"] = False

    if column + len(word) > array.shape[1]:
        possible["left"] = False

    if column + 1 - len(word) < 0:
        possible["right"] = False

    if row + 1 - (len(word) / 2) < 0 or column + (len(word) / 2) > array.shape[1]:
        possible["up+left"] = False

    # Note: Needs diag checks and to all be tested
    print(possible)

    # Now we want to check the possibilities that fit
    for item in possible.items():
        if item[1] == True:
            print("Checking", item[0])
            for i in range(len(word)):
                if translate(row, column, item[0], i, array) == word[i]:
                    print("found:", word[i])
                    if i + 1 == len(word):
                        found = True
                else:
                    print(False, "found:", translate(row, column, item[0], i, array))
                    break
        if found == True:
            print(True, "not checking other places")
            break

    # Input: directions that are possible,
    # Output: if that direction was the word or if it failed
    # For each possibility we need to go in possibility direction

    # if possible["left"] == True:
    #     # Check if the seccond letter is to the left
    #     if array[row, column + 1] == word[1]:
    #         direction = "left"
    #         for i in range(len(word)):
    #             # print("looking for:", word[i])
    #             if array[row][column + i] != word[i]:
    #                 possible["left"] = False
    #             else:
    #                 print("found:", array[row][column + i])


lettersList = [
    ["a", "t", "c", "d", "a", "f"],
    ["p", "h", "i", "o", "k", "l"],
    ["m", "n", "o", "c", "k", "r"],
    ["s", "p", "u", "v", "w", "x"],
]

lettersArray = np.array(lettersList)

print(lettersArray)
word = "poo"

print("Size:", lettersArray.shape[0], "x", lettersArray.shape[1])
print(f"Looking for the word {word}... Looking for the letter {word[0]}")

# Find first letter... Should probably be in the functon... 🎈
for i in range(4):
    for j in range(6):
        current = lettersArray[i][j]
        if current == word[0]:
            print(f"Found {word[0]} at row {i}, col {j}")
            findWord(lettersArray, i, j, word)
