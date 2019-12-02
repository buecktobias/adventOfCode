# Created by Tobias Bück at 2019-12-02 12:54:17.845450
# Solution of day 3 of advent of Code 2019
# 
# INPUTS 
import utility     # helper methods
import inputGetter    # script for getting input file

def get_clean_data():
    with utility.get_input_file(2019, 3) as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)
    return lines_input_file    


def part1():
    lines = get_clean_data()


def part2():
    lines = get_clean_data()   
    
        
def main():
    part1()
    part2()


if __name__ == '__main__':
    main()    
