# Challenge Goal: Count number of fully contained/overlapping task schedules
#
#
import support


# Main function
def main():
    # Read in the file contents
    contents = support.read_input()

    # Read in the pairs of elves
    elf_pairs = contents.split("\n")[:-1]

    # Counter
    fully_contained = 0

    support.start_timer()
    # Split off each pair
    for p in elf_pairs:
        first_elf, second_elf = p.split(",")

        # Find the start and stop of each elf
        first_elf_start, first_elf_stop = [int(x) for x in first_elf.split("-")]
        second_elf_start, second_elf_stop = [int(x) for x in second_elf.split("-")]

        # Convert them to set and compare overlap
        first_set = set(range(first_elf_start, first_elf_stop + 1))
        second_set = set(range(second_elf_start, second_elf_stop + 1))

        # Caculate overlap by taking their union
        combined_set = first_set.union(second_set)

        # Check if the lengths are euqual (indicating a fully contained set)
        if len(combined_set) == len(first_set) or \
            len(combined_set) == len(second_set):
            fully_contained += 1

    print(f"Fully contained sets: {fully_contained}\n")
    support.stop_timer()


# Run the main
if __name__ == "__main__":
    main()
