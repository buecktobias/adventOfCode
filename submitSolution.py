import conf
import requests
import bs4


def submit_solution_requests(year, day, level, answer):
    payload = {'level': level, 'answer': answer}
    r = requests.post(conf.get_url_answer(year, day), cookies=conf.SESSION_COOKIE, data=payload)
    bs = bs4.BeautifulSoup(r.text, features="html.parser")
    text = bs.find("p").text
    print(text)
    # if success:
    # git commit


if __name__ == '__main__':
    submit_solution_requests(2018, 8, 1, "lol")
