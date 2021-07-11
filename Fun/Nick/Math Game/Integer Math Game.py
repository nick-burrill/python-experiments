import random


def setup():  # Setup
    rangeDict = {"oneDigit": False, "twoDigit": False, "threeDigit": False}

    oppDict = {"add": False, "sub": False, "mul": False, "div": False}

    while True:
        digits = int(input("How many digits would you like? (1 - 3): "))

        if digits == 1:
            rangeDict["oneDigit"] = True
            break
        elif digits == 2:
            rangeDict["twoDigit"] = True
            break
        elif digits == 3:
            rangeDict["threeDigit"] = True
            break
        else:
            print("Not in range! (1 - 3)")

    for key in rangeDict:
        if rangeDict[key] == True:
            print(key, "selected")

    for key in oppDict:
        sel = input(f"{key}? (y / n): ")
        if sel == "y":
            oppDict[key] = True
        if sel == "n":
            oppDict[key] = False

    for key in oppDict:
        if oppDict[key] == True:
            print(key, end=" ")

    print("selected")
    return rangeDict, oppDict


def generateNum(rangeDict):  # Generate the numbers
    if rangeDict["oneDigit"] == True:
        start = 0
        end = 9
        step = 1

    if rangeDict["twoDigit"] == True:
        start = 10
        end = 99
        step = 1

    if rangeDict["threeDigit"] == True:
        start = 100
        end = 999
        step = 1

    x = random.randrange(start, end, step)
    y = random.randrange(start, end, step)

    return x, y


def selectOpp(oppDict):  # Select the opperator
    oppList = []

    for i in oppDict:
        if oppDict[i] == True:
            oppList.append(i)

    opp = random.choice(oppList)
    return opp


def solve(x, y, opp):  # Solve the problem
    if opp == "add":
        problem = f"{x} + {y} = ? "
        answer = x + y

    elif opp == "sub":
        problem = f"{x} - {y} = ? "
        answer = x - y

    elif opp == "mul":
        problem = f"{x} * {y} = ? "
        answer = x * y

    elif opp == "div":
        problem = f"{x} / {y} = ? "
        answer = x / y
    else:
        print("Fucking broken")
    return problem, answer


# Do it werk?

rangeDict, oppDict = setup()


while True:
    x, y = generateNum(rangeDict)

    opp = selectOpp(oppDict)

    problem, answer = solve(x, y, opp)

    attempt = int(input(problem))

    if attempt == answer:
        print("Correct!")
    else:
        print("Stupid!")