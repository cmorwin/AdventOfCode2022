# Challenge Goal: Simulate crane operator moving boxes based on Last In
# First Out
#
#
import support


# Main function
def main():
    # Read in the file contents
    contents = support.read_input()

    # Read in the starting positions and instructions
    board_set, instruction_set = contents.split("\n\n")

    # Split up the boards & instructions
    boards = board_set.split("\n")
    instructions = instruction_set.split("\n")[:-1]
    
    support.start_timer()
    # Figure out the number of cargo stacks
    # Each entry looks like '[1] [2]'
    # To make this uniform, we could add an extra space character at the end
    # to give us the following: '[1] [2] ', which means each stack uses 4
    # characters. Similarly, at the bottom of the board, the numbers look like:
    # ' 1   2 ' (len = 7) - simply add 1 and divide by 4
    num_stacks = (len(boards[-1]) + 1) // 4
    
    # Create the current stack (set of lists)
    current_stack = []
    for r in range(num_stacks):
        current_stack.append([])

    # Parse the stacks
    # We'll create lists and start from the bottom of the board, working our way
    # up. The offset into where to look for a block to store is:
    # stack_index * 4 + 1
    # Example: '[1] [2]'
    # stack 1 (index 0), means we look at 0 * 4 + 1 = 1, so string[1]
    # stack 2 (index 1), means we look at 1 * 4 + 1 = 5, so string[5]
    for b in boards[:-1][::-1]:
        for r in range(num_stacks):
            if b[r * 4 + 1] != ' ':
                current_stack[r].append(b[r * 4 + 1])

    # We now have our current stack
    print("Current cargo stack:")
    for r in range(num_stacks):
        print(f"{r}: {current_stack[r]}")
    
    # Go through each instruction
    for i in instructions:
        #  Extract the important numbers
        _, num, _, src, _, dst = i.split(' ')
        num = int(num)
        src = int(src) - 1 # Convert from number to index
        dst = int(dst) - 1 # Convert from number to index

        # Perform the operation
        for o in range(num):
            current_stack[dst].append(current_stack[src].pop())
    
    # We now have our modified stack
    print("\nModified cargo stack:")
    for r in range(num_stacks):
        print(f"{r}: {current_stack[r]}")
    
    # Print results
    print("Top of each stack: ", end="")
    for r in range(num_stacks):
        print(f"{current_stack[r][-1]}", end="")
    print("")
    support.stop_timer()


# Run the main
if __name__ == "__main__":
    main()
