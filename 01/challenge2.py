# Challenge Goal: Count the total amount of Calories carried by the 3 elves
# individually carying the most Calories
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

# Split contents into each elf's inventory
elves = contents.split("\n\n")

# Strip off the final trailing newline (not stripped out by splitting on '\n\n')
elves[-1] = elves[-1][:-1]

# For each elf, sum up their food's Calories
for i in range(0, len(elves)):
    elves[i] = sum([int(i) for i in elves[i].split("\n")])

# Do manual comparisons
start_time = time.process_time()
top3 = [0, 0, 0]
for cal in elves:
    if cal > top3[0]:
        if cal > top3[1]:
            if cal > top3[2]:
                # Highest value - shift everything
                top3[0] = top3[1]
                top3[1] = top3[2]
                top3[2] = cal
            else:
                # 2nd Highest value - shift lower 2
                top3[0] = top3[1]
                top3[1] = cal
        else:
            # 3rd Highest value - replace lowest
            top3[0] = cal
stop_time = time.process_time()

# Print result
print("Method 1: Manual if/else comparisons")
print(f"  Top 3 Calorie counts: {top3[2]}, {top3[1]}, {top3[0]}")
print(f"  Sum of top 3 counts: {sum(top3)}")
print(f"  Calculation took {(stop_time - start_time)*1000:.4} milliseconds")


# Use Python's .sort()
sorted_elves = elves
start_time = time.process_time()
sorted_elves.sort()
stop_time = time.process_time()

# Print result
print("Method 2: Python's .sort() function")
print(
    f"  Top 3 Calorie counts: {sorted_elves[-1]}, {sorted_elves[-2]}, "
    + f"{sorted_elves[-3]}"
)
print(f"  Sum of top 3 counts: {sum(sorted_elves[-3:])}")
print(f"  Calculation took {(stop_time - start_time)*1000:.4} milliseconds")
