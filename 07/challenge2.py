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


# Find all directories above a certain size
def find_directories_above_size(root, size):
    dirs = []

    # If we're already smaller than target size, stop checking subdirectories
    if root.size < size:
        return []
    # Add ourselves to the list
    dirs.append((root.size, root.name))

    # Recursively call all subdirectories
    for d in root.directories:
        dirs += find_directories_above_size(d, size)

    return dirs


# Main function
def main():
    support.start_timer()
    root = generate_filesystem()
    root.calculate_size()

    # Figure out how much space we need to clean up
    max_sys_size = 70000000
    req_free_size = 30000000

    curr_free_size = max_sys_size - root.size

    print(f"We have {curr_free_size:,} bytes available,")
    print(f"but need {req_free_size:,} bytes for the update")
    print(f"We must delete {req_free_size - curr_free_size:,} bytes")

    # Figure out all directories that could be deleted
    dir_to_delete = find_directories_above_size(root, req_free_size - curr_free_size)
    print(f"Found {len(dir_to_delete)} potential directories we could delete")

    # Find the smallest value
    smallest = (root.size, root.name)
    for dd in dir_to_delete:

        if dd[0] < smallest[0]:
            smallest = dd
    
    print(f"Directory to delete: {smallest[1]}, freeing {smallest[0]:,} bytes")
    
    support.stop_timer()


# Run the main
if __name__ == "__main__":
    main()
