range_start, range_end = [int(number) for number in open('../../../input/2019/input4.txt', 'r').read().split('-')]


def password_valid(digits, part1: bool):  # part1 == False means it's part2
    if len(digits) != 6 or len(digits) == len(set(digits)):
        return False
    if not range_start <= int(''.join([str(d) for d in digits])) <= range_end:
        return False
    if not part1 and not any([digits.count(d) == 2 for d in digits]):
        return False
    return True


def generate_passwords(digit_before, digits, part1: bool):  # part1 == False means it's part2
    if password_valid(digits, part1):
        yield digits
    for new_digit in range(digit_before, 9 + 1):
        new_digits = digits + [new_digit]
        if len(new_digits) <= 6:
            pws = generate_passwords(new_digit, new_digits, part1)
            for pw in pws:
                yield pw


passwords_generator1 = generate_passwords(0, [], True)
print(len(list(passwords_generator1)))

passwords_generator2 = generate_passwords(0, [], False)
print(len(list(passwords_generator2)))
