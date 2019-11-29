SESSION = "53616c7465645f5fbccc1d851c18c3e7045654783777b66c2e18feba9f336ccf7864053f8dcb463cd36d9e294ea20528"
SESSION_COOKIE = {"session": SESSION}


def get_url_answer(year, day):
    base_url = "https://adventofcode.com/"
    url = f"{base_url}{year}/day/{day}/answer"
    return url


def get_url(year, day):
    base_url = "https://adventofcode.com/"
    url = f"{base_url}{year}/day/{day}"
    return url
