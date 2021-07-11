import numpy as np


def translate(row, col, direction, array):
    if direction == "left":
        col = col + 1
    if direction == "right":
        col = col - 1
    if direction == "up":
        row = row - 1
    if direction == "down":
        row = row + 1

    return array[row][col]


list = [
    ["a", "b", "c", "d", "e"],
    ["f", "g", "h", "i", "j"],
    ["k", "l", "m", "n", "o"],
    ["p", "q", "r", "s", "t"],
]

array = np.array(list)

print(array)

row = 0
col = 0

print("First letter:", array[row][col])
print("To the left:", translate(row, col, "left", array))
