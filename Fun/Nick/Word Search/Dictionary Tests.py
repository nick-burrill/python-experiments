from typing import get_origin
from rich import print

myDict = {"up": True, "down": True, "right": False}

for i in myDict:
    print(i)

print(myDict)
print(myDict.items)
print(myDict.keys)
print(type(myDict.keys))

for item in myDict.items():
    # print(item)
    print("it just so happens that", item[0], "is set to", item[1])
