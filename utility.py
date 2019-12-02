def get_lines_of_file(file):
    return file.read().split("\n")


def get_lines_as_ints(file):
    return [int(line) for line in file.read().split("\n") if line != ""]


def get_input_file(year, day):
    return open(f"input/{year}/input{day}.txt")
