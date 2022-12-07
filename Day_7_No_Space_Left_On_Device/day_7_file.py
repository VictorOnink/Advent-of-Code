from pathlib import Path

def load_puzzle_input(case: str) -> list:
    if case == 'test':
        file_name = "Day_7_No_Space_Left_On_Device/test_input.txt"
    elif case == 'puzzle':
        file_name = "Day_7_No_Space_Left_On_Device/puzzle_input.txt"
    with open(file_name) as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

def get_directory_structure(commands: list) -> dict:
    current_level = Path("")
    directory_structure = {}

    for entry in commands:
        # Moving around directories
        if "$ cd" in entry:
            # The case when we move up a directory
            if ".." in entry:
                current_level = current_level.parent
            # The case when we move to a target
            else:
                direc_name = entry[5:]
                current_level = current_level / direc_name
                if current_level not in directory_structure.keys():
                    directory_structure[current_level] = []
        # If the command starts with dir, it means this path is at current level
        elif "dir" in entry:
            _, direc_name = entry.split(" ")
            directory_structure[current_level].append(current_level / direc_name)
        elif entry[0].isnumeric():
            file_size, file_name = entry.split(" ")
            directory_structure[current_level].append((file_name, int(file_size)))
        

    return directory_structure

def get_directory_size(directory_structure: dict, size_threshold: int) -> dict:
    sum_size_under_threshold = 0
    all_directory_sizes = {}
    for directory in directory_structure.keys():
        directory_size = total_directory_size(directory, directory_structure)
        all_directory_sizes[directory] = directory_size
        if directory_size < size_threshold:
            sum_size_under_threshold += directory_size

    print(f"The sum of folder sizes under threshold {size_threshold} is {sum_size_under_threshold}")

    return all_directory_sizes

def total_directory_size(folder_path: Path, directory_structure: dict) -> int:
    total_size = 0
    for object in directory_structure[folder_path]:
        if isinstance(object, tuple):
            total_size += object[1]
        elif isinstance(object, Path):
            total_size += total_directory_size(object, directory_structure)
    return total_size

def find_minimum_deletable_size(all_directory_sizes: dict) -> None:
    total_space_disk = 70000000
    total_space_used = all_directory_sizes[Path("/")]
    initial_free_space = total_space_disk - total_space_used
    required_space = 30000000
    clearable_space = required_space - initial_free_space

    print(f"\n\nWe use {total_space_used}/{total_space_disk}, which means we need to clear {clearable_space}")
    minimum_removeable_folder = (70000000, Path("Random/Path"))

    for directory_name in all_directory_sizes.keys():
        if all_directory_sizes[directory_name] >= clearable_space:
            if all_directory_sizes[directory_name] < minimum_removeable_folder[0]:
                minimum_removeable_folder = (all_directory_sizes[directory_name], directory_name)
    
    print(f"Deleting {minimum_removeable_folder[1]} would clear up {minimum_removeable_folder[0]} storage.")


if __name__ == "__main__":
    # commands = load_puzzle_input('test')
    commands = load_puzzle_input('puzzle')

    directory_structure = get_directory_structure(commands)

    all_directory_sizes = get_directory_size(directory_structure, 100000)

    find_minimum_deletable_size(all_directory_sizes)


