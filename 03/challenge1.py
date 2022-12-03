# Challenge Goal: Determine the sum of the priorities of mixed items in elf
# rucksacks
#
#
import support


# Return the priority value for the given character
def get_priority(c):
    # Convert the character to an int
    char_ord = ord(c)

    # Move capital letters above lower case letters
    if char_ord < ord("a"):
        char_ord += (ord("a") - ord("A")) + 26

    # Normalize to 1-26 & 27-52
    char_ord -= ord("a") - 1

    # Return result
    return char_ord


# Main function
def main():
    # Read in the file contents
    contents = support.read_input()

    # Split contents into each rucksack
    rucksacks = contents.split("\n")[:-1]  # Remove double newline
    print(f"Found {len(rucksacks)} rucksacks\n")

    # Start timer and initialize total_priority
    support.start_timer()
    total_priority = 0

    # Loop through each rucksack
    for r in rucksacks:
        # Divide the rucksacks into 2 groups of contents
        middle = int(len(r) / 2)
        first_compartment = r[:middle]
        second_compartment = r[middle:]

        # Figure out which items are in both components
        # We first convert the first_compartment into a set
        # We then do an intersection of the set with the second_compartment
        overlap = set(first_compartment).intersection(second_compartment)

        # Get the priorities for each item in our calculated overlap
        for o in overlap:
            total_priority += get_priority(o)

    # Print result
    print(f"Total priority: {total_priority}")
    support.stop_timer()


# Run the main
if __name__ == "__main__":
    main()
