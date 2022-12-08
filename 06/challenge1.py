# Challenge Goal: Find the start-of-packet marker, which is 4 consecutive,
# unique characters
#
#
import support


# Main function
def main():
    # Read in the file contents
    contents = support.read_input()

    curr_pos = 0
    marker_length = 14
    
    support.start_timer()
    while True:
        if len(set(contents[curr_pos:curr_pos + marker_length])) < marker_length:
            curr_pos += 1
        else:
            curr_pos += marker_length
            break
    print(f"Found start-of-packet at position: {curr_pos}")
    support.stop_timer()


# Run the main
if __name__ == "__main__":
    main()
