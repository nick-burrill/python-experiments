import random

done = False
while done == False:
    userinput = input("rock, paper, or scissors?   ")
    CPU = ["rock", "paper", "scissors"]
    random.shuffle(CPU)

    if CPU[0] == "rock":
        print("the cpu chose", CPU[0])
        if userinput == "paper" or "Paper":
            print("You Won!")
        if userinput == "scissors" or "Scissors":
            print("You Lost!")
        if userinput == "rock" or "Rock":
            print("Tie!")

    if CPU[0] == "paper":
        print("the cpu chose", CPU[0])
        if userinput == "paper" or "Paper":
            print("Tie!")
        if userinput == "scissors" or "Scissors":
            print("You Won!")
        if userinput == "rock" or "Rock":
            print("You Lost!")

    if CPU[0] == "scissors":
        print("the cpu chose", CPU[0])
        if userinput == "paper" or "Paper":
            print("You Lost!")
        if userinput == "scissors" or "Scissors":
            print("Tie!")
        if userinput == "rock" or "Rock":
            print("You Won!")
    doneq = input("are you done? (Y/N)")
    if doneq == "Y":
        done = True
        print("thanks for playing")
