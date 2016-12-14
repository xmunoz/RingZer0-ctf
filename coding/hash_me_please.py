import requests
from lxml import html
import hashlib
import os


def main():
    '''
    Solution to "Hash me if you can".
    Requires that you set an environment variable PHPSESSID.
    '''
    BASE_URL = "https://ringzer0team.com/challenges/13/"
    cookie = {
        "PHPSESSID": os.getenv("PHPSESSID"),
    }
    response = requests.get(BASE_URL, cookies=cookie)
    tree = html.fromstring(response.content)
    message = tree.xpath("/html/body/div[2]/div/div[2]/div/text()[2]")[0]
    message = message.strip()

    result = hashlib.sha512(message.encode("utf-8")).hexdigest()
    url = BASE_URL + result
    r = requests.get(url, cookies=cookie)

    response_tree = html.fromstring(r.content)
    flag = response_tree.xpath("/html/body/div[2]/div/div[2]/div[1]")[0]
    print(flag.text)


if __name__ == "__main__":
    main()
