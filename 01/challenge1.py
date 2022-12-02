# Challenge Goal: Count the largest amount of Calories carried by a single elf
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


# For each elf, add up their food's Calories, only keeping the highest total
start_time = time.process_time()
max_calories = 0
for elf in elves:
    foods = [int(i) for i in elf.split("\n")]
    total_calories = sum(foods)
    if total_calories > max_calories:
        max_calories = total_calories
stop_time = time.process_time()

# Print result
print("Method 1: Manual 'if > max' comparisons")
print(f"  Max Calories carried by an elf: {max_calories}")
print(f"  Calculation took {(stop_time - start_time)*1000:.4} milliseconds")


# For each elf, add up their food's Calories
start_time = time.process_time()
for i in range(0, len(elves)):
    elves[i] = sum([int(i) for i in elves[i].split("\n")])
max_calories = max(elves)
stop_time = time.process_time()

# Print result
print("Method 2: Python's max() function")
print(f"  Max Calories carried by an elf: {max_calories}")
print(f"  Calculation took {(stop_time - start_time)*1000:.4} milliseconds")
