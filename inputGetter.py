import requests
import os


def get_input(year, day):
    path = f"input/input{day}.txt"
    base_url = "https://adventofcode.com/"
    url = f"{base_url}{year}/day/{day}/input"
    session = "53616c7465645f5fbccc1d851c18c3e7045654783777b66c2e18feba9f336ccf7864053f8dcb463cd36d9e294ea20528"
    r = requests.post(url, cookies={"session": session})
    with open(path, "w") as file:
        if r.status_code == 200:
            file.write(r.text)
        else:
            raise ValueError(f"{r.status_code} {r.text}")


def create_script(day):
    day_directory = f"src/day{day}"
    try:
        os.mkdir(day_directory)
    except FileExistsError:
        pass
    path = day_directory + "/main.py"
    f = open(path, "w")
    f.close()


def prepare(year, day):
    create_script(day)
    get_input(year, day)


if __name__ == '__main__':
    prepare(2018, 1)

