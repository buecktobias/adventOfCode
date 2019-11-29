import requests
import os
import conf
import datetime
import subprocess


def make_template(year, day):
    date = datetime.datetime.now()
    return f"""
# Created by Tobias Bück at {str(date)}
# Solution of {day} of advent of Code {year}
# 
# INPUTS 
import utility     # helper methods
import inputGetter    # script for getting input file
import submitSolution   # script to submit uploading solution


# opens the input file
def get_input_file():
    return open("../../../{input_path(year, day)}")


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
    submitSolution.submit_solution_requests({year}, {day}, level, solution)


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
        os.mkdir(day_directory)
    except FileExistsError:
        pass
    path = day_directory + "/main.py"
    f = open(path, "w")
    f.write(make_template(year, day))
    f.close()
    # add to git
    os.system("git init")
    os.system(f"git add {path}")
    os.system(f"git commit -m \"created script for day {day}\"")

def prepare(year, day):
    create_script(year, day)
    get_input(year, day)


if __name__ == '__main__':
    prepare(2018, 1)

