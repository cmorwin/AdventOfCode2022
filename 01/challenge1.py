# Challenge Goal: Count the largest amount of Calories carried by a single elf
#
#

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
max_calories = 0
for elf in elves[:-1]:
    foods = [int(i) for i in elf.split("\n")]
    total_calories = sum(foods)
    if total_calories > max_calories:
        max_calories = total_calories

# Print result
print(f"Max Calories carried by an elf: {max_calories}")
