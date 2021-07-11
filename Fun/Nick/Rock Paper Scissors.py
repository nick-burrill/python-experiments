import random

# MAIN GOAL:
# We need to compare two inputs with 3 possibilities and decide the winner
# We should keep track of who gave us the input to declare them as winner


def printOutputs():  # Only used for clarification
    rock = 0
    paper = 1
    scissors = 2

    print("== ROCK VS PAPER ==")
    print("Player 1 wins:", paper - rock)
    print("Player 2 wins:,", rock - paper)

    print("== PAPER VS SCISSORS ==")
    print("Player 1 wins:", scissors - paper)
    print("Player 2 wins:", paper - scissors)

    print("== SCISSORS VS ROCK ==")
    print("Player 1 wins:", rock - scissors)
    print("Player 2 wins:", scissors - rock)

    print("== TIES ==")
    print("Scissor:", scissors - scissors)
    print("Rock:", rock - rock)
    print("Paper:", paper - paper)


# printOutputs() # Uncomment if you need to know how it works


def getString(index):  # Because we are always returning strings we print this function
    if index == 0:
        return "rock"
    if index == 1:
        return "paper"
    if index == 2:
        return "scissors"


running = True
while running:
    cpu = random.randint(0, 2)
    print("CPU:", getString(cpu))  # Take the guessing out of debug
    player = int(input("Choose rock:0, paper:1, scissors:2, quit:3 \n"))

    if player == 3:  # Quit
        running = False
        print("Goodbye...")
        break

    print(
        getString(cpu), "V.S.", getString(player)
    )  # Using the swag function to tell the user whats poppin

    score = cpu - player  # Refer to printOutputs()
    if score == 0:
        print("Tie")
    if score == -1 or score == 2:
        print("Player wins")
    if score == 1 or score == -2:
        print("CPU wins")