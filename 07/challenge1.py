# Challenge Goal: 
#
#
from __future__ import annotations
import support


# Directory class to track details
class Directory:
    # Init
    def __init__(self, name:str, parent:Directory):
        self.name = name
        self.parent = parent
        self.directories = []
        self.files = {}
        self.size = 0

    # Add a directory
    def add_directory(self, new_dir:str):
        for d in self.directories:
            if d.name == new_dir:
                return
        dir_to_add = Directory(new_dir, self)
        self.directories.append(dir_to_add)

    # Add files
    def add_file(self, file_name:str, file_size:int):
        if file_name not in self.files:
            self.files[file_name] = file_size

    # Calculate size
    def calculate_size(self):
        self.size = sum(self.files.values())
        if len(self.directories) > 0:
            for d in self.directories:
                d.calculate_size()
                self.size += d.size
    
    # Print visual tree
    def print(self, nest=0):
        print(" " * nest + f"{self.name} (dir)")
        for f in self.files:
            print(" " * (nest + 1) + f"{f}: {self.files[f]}")
        for d in self.directories:
            d.print(nest + 1)


# Read in the filesystem
def generate_filesystem() -> Directory:
    # Read in the file contents
    contents = support.read_input()

    # Setup root, since we know it must exist
    root = Directory("/", None)
    
    # Track our current directory
    curr_dir = None

    # Read our lines of input
    lines = contents.split("\n")[:-1]
    curr_line = 0
    while curr_line < len(lines):
        command = lines[curr_line]

        # Process 'cd'
        if  "$ cd" in command:
            dir = command[5:]
            if dir == "/":
                curr_dir = root
            elif dir == "..":
                curr_dir = curr_dir.parent
            else:
                for d in curr_dir.directories:
                    if dir == d.name:
                        curr_dir = d
                        break
            curr_line += 1
            # Done processing 'cd'
            continue

        # Process 'ls'
        if "$ ls" in command:
            curr_line += 1
            # Process everything until the next command
            while "$ " != lines[curr_line][:2]:
                if "dir" in lines[curr_line]:
                    curr_dir.add_directory(lines[curr_line][4:])
                else:
                    file_size, file_name = lines[curr_line].split(' ')
                    curr_dir.add_file(file_name, int(file_size))
                curr_line += 1
                # Make sure we stay in bounds
                if curr_line >= len(lines):
                    break
            # Done processing 'ls'
            continue

        # Uh.... something broke? Print & quit
        print(f"ERROR: Unknown line: {lines[curr_line]}")
        return None

    return root


# Sum up the size of each directory if its below a certain size
def sum_directories_below_size(root, size) -> int:
    total_size = 0

    for d in root.directories:
        if d.size < size:
            total_size += d.size
        total_size += sum_directories_below_size(d, size)
    
    return total_size


# Main function
def main():
    support.start_timer()
    root = generate_filesystem()
    root.calculate_size()
    summed_size = sum_directories_below_size(root, 100000)
    print(f"Total size: {summed_size}")
    support.stop_timer()


# Run the main
if __name__ == "__main__":
    main()
