# Challenge Goal: Determine the sum of the priorities of the badges carried by
# each set of 3 elves
#
#
import support

# Return the priority value for the given character
def get_priority(c):
    char_ord = ord(c)
    # Move capital letters above lower case letters
    if char_ord < ord("a"):
        char_ord += (ord("a") - ord("A")) + 26

    # Normalize to 1-26 & 27-52
    char_ord -= ord("a") - 1
    return char_ord


def main():
    # Read in the file contents
    contents = support.read_input()

    # Split contents into each rucksack
    rucksacks = contents.split("\n")[:-1]  # Remove double newline
    print(f"Found {len(rucksacks)} rucksacks\n")

    # Start timer and initialize total_priority & counter
    support.start_timer()
    total_priority = 0
    counter = 0

    # Since we're working on sets of 3, we're going to use an index that we
    # increase by 3 on each loop. Its simple and only works if the input array
    # is evenly divisible by 3, else we hit an IndexError. We'll accept this
    # risk because the problem made no mention of what to do for elf teams that
    # weren't full, so we're assuming they are.
    while counter < len(rucksacks):
        # Calculate overlap of first two elves
        overlap = set(rucksacks[counter]).intersection(rucksacks[counter + 1])

        # Calculate shared overlap of the 3rd elf
        overlap = overlap.intersection(rucksacks[counter + 2])

        # There should only be 1 matching item, but we'll assume that instead
        # of checking, since the problem made no mention of what to do if there
        # were multiple matches (i.e. 'the higher priority item is the badge')
        for o in overlap:
            total_priority += get_priority(o)

        # Increment the counter
        counter += 3

    # Print result
    print(f"Total priority: {total_priority}")
    support.stop_timer()


# Run main
if __name__ == "__main__":
    main()
