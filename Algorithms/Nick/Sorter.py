import random
import time

Range = 1000  # size of list, use with caution

x = list(range(1, Range + 1))
random.shuffle(x)
print(x)

changes = 0  # how many changes to sort it
Loop = 0  # how many loops to sort it
CI = 0  # Current Index
NA = 0  # Number A
NB = 1  # Number B
MEM = NB  # Used for switching nums
Streak = 0  # helps to tell if sorted
sorted = False
# Added to keep track of efficency
MaxStreak = 0
WasteMoves = 0  # Counts every streak of zero
TimeRemaining = 0  # Predicts the time remaining
TimeSort = []  # Time it takes to increase max streak
AvgTimeSort = 0  # Avg time to increase max streak. used for prediction
TIMEOLD = float(time.perf_counter())  # old time for measuring

while sorted == False:
    if CI == Range - 1:
        CI = 0
        Loop = Loop + 1
        if Streak > Range - 1:
            sorted = True
            print("Sorted into", x, "after", Loop, "loops, with", changes, "changes")

    NA = x[CI]
    NB = x[CI + 1]

    if NA + 1 == NB:
        CI = CI + 1
        Streak = Streak + 1
    else:
        # print (x)
        if NA > NB:
            x[CI + 1] = NA
            x[CI] = NB
        if NA < NB:
            x[CI + 1] = NB
            x[CI] = NA
        CI = CI + 1

        if Streak > MaxStreak:
            NewTime = float(time.perf_counter())  # Added here to ignore my bs below
            MaxStreak = Streak
            TimeSort.append(NewTime - TIMEOLD)  # Find difference in time
            AvgTimeSort = (AvgTimeSort + NewTime) / 2  # Add to average time taken
            TimeRemaining = (Range - MaxStreak) * AvgTimeSort  # Assume linear sorting
            print(
                "Max Streak",
                MaxStreak,
                "Took:",
                TimeSort[-1:],
                "Avg:",
                AvgTimeSort,
                "Remaining:",
                TimeRemaining,
                "Waste:",
                WasteMoves,
            )
            Streak = 0
            TIMEOLD = float(time.perf_counter())  # Reset timer
        elif Streak < 1:
            WasteMoves += 1

        Streak = 0
        changes = changes + 1