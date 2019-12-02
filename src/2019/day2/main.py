import random
# Created by Tobias Bück at 2019-12-02 06:05:30.339167
# Solution of day 2 of advent of Code 2019
# 
# INPUTS 
import utility     # helper methods
import inputGetter    # script for getting input file
import submitSolution   # script to submit uploading solution


# opens the input file
def get_input_file():
    return open("../../../input/2019/input2.txt")


def get_numbers():
    input_file = get_input_file()
    lines_input_file = utility.get_lines_of_file(input_file)
    numbers = "".join(lines_input_file)
    numbers = list(numbers.split(","))
    numbers = list([int(number) for number in numbers])
    input_file.close()
    return numbers


def calculate(numbers):
    for i in range(0, len(numbers), 4):
        if numbers[i] == 1:
            ergebnis = numbers[numbers[i + 1]] + numbers[numbers[i + 2]]
            numbers[numbers[i + 3]] = ergebnis
        elif numbers[i] == 2:
            ergebnis = numbers[numbers[i + 1]] * numbers[numbers[i + 2]]
            numbers[numbers[i + 3]] = ergebnis
        elif numbers[i] == 99:
            break
        else:
            print("broken")
            break
    return numbers


# solve days puzzle
def solve():
    solution = 0
    numbers = get_numbers()

    for number1 in range(100):
        for number2 in range(100):
            numbers[1] = number1
            numbers[2] = number2
            try:
                numbers = calculate(numbers)
            except:
                pass
            if numbers[0] == 19690720:
                print(numbers[1])
                print(numbers[2])
                return
            numbers = get_numbers()



    return solution
    
    
def main():
    solution = solve()
    level = 1  # level of the day, part, every day has two parts
    #submitSolution.submit_solution_requests(2019, 2, level, solution)


if __name__ == '__main__':
    main()    
