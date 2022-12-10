from typing import List

def load_puzzle_input(case: str) -> List[str]:
    if case == "puzzle":
        file_name = "Day_10_Cathode_Ray_Tube/puzzle_input.txt"
    else:
        file_name = "Day_10_Cathode_Ray_Tube/test_input.txt"
    with open(file_name) as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

def print_screen(lines: List[str], signal_selection: List[int]):
    register: int = 1
    cycle: int = 1
    signal_strengths: List[str] = [register * cycle]

    screen_pixels = ""

    for line in lines:
        screen_pixels = print_pixel(screen_pixels, cycle, register)
        cycle += 1
        signal_strengths.append(register * cycle)
        
        if "addx" in line:
            screen_pixels = print_pixel(screen_pixels, cycle, register)           
            cycle += 1
            register += int(line.split()[1])
            signal_strengths.append(register * cycle)
            


    sum_selected_signal_strengths = sum(signal_strengths[i] for i in signal_selection)

    print(f"We have {sum_selected_signal_strengths=}")

    print(screen_pixels)

    

def print_pixel(screen_pixels, cycle, register):
    if abs(((cycle - 1) % 40 - register)) <= 1:
        screen_pixels += "#"
    else:
        screen_pixels += "."
    if (cycle - 1) % 40 == 39:
        screen_pixels += "\n"
    return screen_pixels

if __name__ == "__main__":
    lines = load_puzzle_input("puzzle")

    signal_selection = [19, 59, 99, 139, 179, 219]
    print_screen(lines, signal_selection)
    
