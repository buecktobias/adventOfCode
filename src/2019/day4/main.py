# Created by Tobias Bück at 2019-12-04 06:03:07.047200
# Solution of day 4 of advent of Code 2019
# 
# INPUTS 
import utility     # helper methods


def get_input_file():
    return open("../../../input/2019/input4.txt")


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)
    return lines_input_file    


def has_increasing_digits(str_number):
    for i in range(1, len(str_number)):
        if int(str_number[i]) < int(str_number[i-1]):
            return False
    return True


def has_double_adjacent(str_number):
    for i in range(1, len(str_number)):
        if int(str_number[i]) == int(str_number[i-1]):
            return True
    return False


def has_only_2_adjacent(str_number):
    for i in range(1, len(str_number)):
        if int(str_number[i]) == int(str_number[i-1]):
            if i - 2 >= 0 and int(str_number[i-2]) == int(str_number[i]):
                continue
            if i + 1 < len(str_number) and int(str_number[i +1]) ==  int(str_number[i]):
                continue
            return True
    return False


def is_correct_password_part1(password):
    str_password = str(password)
    return has_increasing_digits(str_password) and has_double_adjacent(str_password)


def is_correct_password_part2(password):
    str_password = str(password)
    return has_increasing_digits(str_password) and has_only_2_adjacent(str_password)


def part1():

    START = 168630
    END = 718098
    numbers_valid = 0

    for number in range(START, END):
        if is_correct_password_part1(number):
            numbers_valid += 1

    return numbers_valid


def part2():
    START = 168630
    END = 718098
    numbers_valid = 0

    for number in range(START, END):
        if is_correct_password_part2(number):
            numbers_valid += 1

    return numbers_valid
    
        
def main():
    print(f"part1: " + str(part1()))
    print(f"part2: " + str(part2()))


if __name__ == '__main__':
    print(is_correct_password_part2(111334))
    main()    
