from rich import print

ratio = "2.5m / sec" # input("Enter a ratio for me to convert: ")

num1 = 0.0
unit1 = ""
num2 = ""
unit2 = ""
firstDict = {}




firstHalf = ''
seccondHalf = ''
for i in range(len(ratio)):
    if ratio[i] == "/":
        firstHalf = ratio[:i]
        seccondHalf = ratio[i+1:]

def detatch(string, dict):
    unit = ''
    num = 0.0
    for i in range(len(string)):
        if string[i].isalpha():
            unit += string[i]
        else:
            if string[i].isnumeric():
                numstr += string[
    
    dict[unit] = num
    
detatch(firstHalf, firstDict)
#detatch(seccondHalf, firstDict)

print(firstDict)

print(firstHalf , "\n", seccondHalf)
print("num1:", num1)
print("unit1:", unit1)
