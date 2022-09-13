# This is gonna be the word search creator until I decide I want to combine them
# First we need to ask the user how many words they want to input, 0 means we will keep asking until they put another 0 in the input
# Next we want to dump the words in the array where they are possible, starting with bigger words first
# I can already tell this is gonna be kind of dumb and just bogo sorting
# Fill with random letters, or optionally random slices of the words you entered

from rich import print
import numpy as np
import random

print("Creating array...")
gridShape = (10, 10)
array = np.zeros(gridShape)
array = array.astype(int)
array = array.astype(str)
print(array)

list = ["hello", "world", "nicholas", "wordsearch"]


def checkPossible(row, col, word, array):
    # Next we do a pre-check, eliminate any out of bounds options
    if row + 1 - len(word) < 0:
        possible["up"] = False
    if row + len(word) > array.shape[0]:
        possible["down"] = False
    if col + len(word) > array.shape[1]:
        possible["left"] = False
    if col + 1 - len(word) < 0:
        possible["right"] = False
    if row + 1 - len(word) < 0 or col + len(word) > array.shape[1]:
        possible["up+left"] = False


def translate(row, col, direction, distance, array, mode):
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

    if row + 1 > array.shape[0] or col + 1 > array.shape[1] or row < 0 or col < 0:
        print("Out of bounds buddy!", end=" ")
        print((row, col))
    else:
        if mode == 0:
            return array[row][col]
        if mode == 1:
            return (row, col)


for word in list:
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
    print("adding:", word)
    # Choose starting point > Determine if possible, repeat if not > Continue in that direction
    row = random.randint(0, gridShape[0] - 1)
    col = random.randint(0, gridShape[1] - 1)
    checkPossible(row, col, word, array)
    print(possible)
    for item in possible.items():
        if item[1] == True:
            print(f"Going {item[0]}")
            tempArray = array
            for i in range(len(word)):
                where = translate(row, col, item[0], i, tempArray, 1)
                # where = (where[0] + 1, where[1] - 1)
                if where != None:
                    if tempArray[where] == "0":
                        print(word[i], end=" ")
                        tempArray[where] = word[i]
                        print(where)
                        if i == len(word):
                            print("breaking")
                            break
                    else:
                        print("Obstruction!", end=" ")
                        print(where)
                        break
    print(array)
