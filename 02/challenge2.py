# Challenge Goal: Calculate the helpful elf's Rock-Paper-Scissors (RPS)
# strategy score
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
# If the outcome is 0 (we lose), then we get the following points based
# on our opponent's choice:
# A = 3, B = 1, C = 2
#
# If the outcome is 1 (we tie), then we get the following points based
# on our opponent's choice:
# A = 1, B = 2, C = 3
#
# If the outcome is 2 (we win), then we get tthe following points based
# on our opponent's choice:
# A = 2, B = 3, C = 1
#
# Using this info, we can create a lookup table to figure out how many points
# we should get for any given combination
score_chart = [[0, 3, 1, 2],
               [0, 1, 2, 3],
               [0, 2, 3, 1]]
# (we have leading zeros, because we're going to address the table with
# score_chart[0-2][1-3], rather than score_chart[0-2][0-2], and rather than
# dealing with an additional subtraction every single lookup, we just allocate
# a little more memory for our table)


for r in rounds[:-1]: # Ignore the last round which is empty due to double newline
    # We're going to convert the characters to integers
    # We do this by getting the ordinal of the character
    # ('A' = 65, 'B' == 66, 'C' == 67, 'X' == 88, 'Y', == 89, 'Z' == 90)
    # We normalize these so A == 1, B == 2, C == 3,
    # and X == 0, Y == 1, Z == 2 (this range is different than A,B,C now)
    opponent = ord(r[0]) - ord('A') + 1
    outcome = ord(r[-1]) - ord('X')
    
    # Directly add points for our RPS outcome (3 x outcome = 0, 3 or 6)
    # This could have been pre calculated like in challenge1.py, but I took
    # a different approach for the sake of taking a different approach
    total_score += 3 * outcome
    
    # Lookup our scores
    total_score += score_chart[outcome][opponent]
stop_time = time.process_time()


# Print result
print("Method 1: Lookup score chart")
print(f"  Total score: {total_score}")
print(f"  Calculation took {(stop_time - start_time)*1000:.4} milliseconds")
