# Created by Tobias Bück at 2019-12-18 14:16:25.534081
# Solution of day 16 of advent of Code 2019
# 
# INPUTS 
import utility     # helper methods

def get_input_file():
    return open("../../../input/2019/input16.txt")

def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)
    return lines_input_file    


def part1():
    lines = get_clean_data()


def part2():
    lines = get_clean_data()   
    
        
def main():
    print(f"part1: " + part1())
    print(f"part2: " + part2())


if __name__ == '__main__':
    main()    
