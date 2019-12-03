import requests
import os
import conf
import datetime


def make_template(year, day):
    date = datetime.datetime.now()
    return f"""# Created by Tobias Bück at {str(date)}
# Solution of day {day} of advent of Code {year}
# 
# INPUTS 
import utility     # helper methods

def get_input_file():
    return open("../../../input/{year}/input{day}.txt")

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
"""


def input_path(year, day):
    return f"input/{year}/input{day}.txt"


def get_input(year, day):
    path = input_path(year, day)
    try:
        os.mkdir(f"input/{year}")
    except FileExistsError:
        pass
    url = conf.get_url(year, day) + "/input"
    r = requests.post(url, cookies=conf.SESSION_COOKIE)
    if r.status_code == 200:
        with open(path, "w") as file:
            file.write(r.text)
        os.system("git init")
        os.system(f"git add {path}")
        os.system(f"git commit -m \"Downloaded input file of day {day}\"")
    else:
        raise ValueError(f"{r.status_code} {r.text}")


def create_script(year, day):
    day_directory = f"src/{year}/day{day}"
    try:
        os.mkdir(f"src/{year}")
    except FileExistsError:
        pass

    try:
        os.mkdir(day_directory)
    except FileExistsError:
        pass
    path = day_directory + "/main.py"
    f = open(path, "x")
    f.write(make_template(year, day))
    f.close()
    # add to git
    os.system("git init")
    os.system(f"git add {path}")
    os.system(f"git commit -m \"created script for day {day}\"")


def prepare(year, day):
    #create_script(year, day)
    get_input(year, day)


if __name__ == '__main__':
    prepare(2019, 3)

