
# Created by Tobias Bück at 2019-11-29 23:19:54.249226
# Solution of 1 of advent of Code 2018
# 
# INPUTS 
import utility     # helper methods
import inputGetter    # script for getting input file
import submitSolution   # script to submit uploading solution


# opens the input file
def get_input_file():
    return open("../../../input/2018/input1.txt")


# solve days puzzle
def solve():
    solution = 0
    input_file = get_input_file()
    lines_input_file = utility.get_lines_of_file(input_file)
    
    
    input_file.close()
    return solution
    
    
def main():
    solution = solve()
    level = 1  # level of the day, part, every day has two parts
    submitSolution.submit_solution_requests(2018, 1, level, solution)


if __name__ == '__main__':
    main()    
