import numpy as np

width = 10
height = 20
array = [[0] * width] * height

print(array)

for i in range(height):
    for j in range(width):
        array[i][j] = "test"

print(array)

# Need to create a numpy array and fill
