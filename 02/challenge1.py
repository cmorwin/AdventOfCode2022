# Challenge Goal: Calculate our Rock-Paper-Scissors (RPS) strategy score
#
#
# We're going to time a couple methods for fun
import time

# Read in the file contents
try:
    with open("input.txt", "r") as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found")
    exit

# Split contents into each round of RPS
rounds = contents.split("\n")
print(f"Found {len(rounds) - 1} rounds to play\n")

# Keep track of our score
total_score = 0


start_time = time.process_time()
for r in rounds[:-1]:  # Ignore the last round which is empty due to double newline
    # We're going to convert the characters to integers
    # We do this by getting the ordinal of the character
    # ('A' = 65, 'B' == 66, 'C' == 67, 'X' == 88, 'Y', == 89, 'Z' == 90)
    # We normalize these so A == X == 1, B == Y == 2, C == Z == 3
    opponent = ord(r[0]) - ord("A") + 1
    us = ord(r[-1]) - ord("X") + 1

    # Directly add points for our RPS choice
    total_score += us

    # Calculate for a draw
    if opponent == us:
        total_score += 3
        continue

    # Calculate if we won or lost the round
    # <<Rock Paper Scissors (input pair) [normalized ord]>>
    # Our winning pairs: R P (A Y) [1 2] / P S (B Z) [2 3] / S R (C X) [3 1]
    # If we subtract our normalized ord from the opponents, we get 1 or -2
    #
    # Losing pairs: R S (A, Z) [1 3] / P R (B, X) [2 1] / S P (C Y) [3 2]
    # If we subtract the ords, we get 2 or -1
    #
    # Rather than doing 3 checks, to look for all 3 possibilities of either
    # a win or a loss, we only need to do some simple math and make 2 checks
    diff = us - opponent
    if diff == 1 or diff == -2:
        total_score += 6
stop_time = time.process_time()


# Print result
print("Method 1: Subtracting normalized ords")
print(f"  Total score: {total_score}")
print(f"  Calculation took {(stop_time - start_time)*1000:.4} milliseconds")


total_score = 0
start_time = time.process_time()
# The opponent has 3 choices and we have 3 choices, giving us 9 total outcomes
# We can pre-generate all the points in a table and do simple table lookups
# For this, we'll normalize the inputs using their ordinals
# A == X == 3, B == Y == 1, C == Z == 2
#
# If the opponent chooses A (rock), we get the following points:
# X==1 + tie==3 = 4, Y==2 + win==6 = 8, Z==3 + lose==0 = 3
#
# If the opponent chooses B (paper), we get the following points:
# X==1 + lose==0 = 1, Y==2 + tie==3 = 5, Z==3 + win==6 = 9
#
# If the opponent chooses C (scissors), we get the following points:
# X==1 + win==6 = 7, Y==2 + lose==0 = 2, Z==3 + tie==3 = 6
#
# Using this info, we can create a lookup table to figure out how many points
# we should get for any given combination
score_chart = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]

for r in rounds[:-1]:  # Ignore the last round which is empty due to double newline
    # We're going to convert the characters to integers
    # We do this by getting the ordinal of the character
    # ('A' = 65, 'B' == 66, 'C' == 67, 'X' == 88, 'Y', == 89, 'Z' == 90)
    # We normalize these so A == X == 0, B == Y == 1, C == Z == 2
    opponent = ord(r[0]) - ord("A")
    us = ord(r[-1]) - ord("X")

    # Directly add points for our RPS choice
    total_score += score_chart[opponent][us]
stop_time = time.process_time()

# Print result
print("Method 1: Lookup table")
print(f"  Total score: {total_score}")
print(f"  Calculation took {(stop_time - start_time)*1000:.4} milliseconds")
