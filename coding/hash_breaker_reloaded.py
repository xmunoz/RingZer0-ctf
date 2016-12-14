import requests
from lxml import html
import hashlib
import os


def main():
    '''
    Solution to "Hash breaker reloaded".
    Requires that you set an environment variable PHPSESSID.
    '''
    BASE_URL = "https://ringzer0team.com/challenges/57/"
    cookie = {
        "PHPSESSID": os.getenv("PHPSESSID"),
    }
    response = requests.get(BASE_URL, cookies=cookie)
    tree = html.fromstring(response.content)
    message_hash = tree.xpath("/html/body/div[2]/div/div[2]/div/text()[2]")[0]
    message_hash = message_hash.strip()
    salt = tree.xpath("/html/body/div[2]/div/div[2]/div[2]/text()[2]")[0]
    salt = salt.strip()

    for i in range(1, 10000):
        # salt can come before or after the main message
        hash_str = str(i) + salt
        result = hashlib.sha1(hash_str.encode("utf-8")).hexdigest()
        if result == message_hash:
            break

    url = BASE_URL + str(i)
    r = requests.get(url, cookies=cookie)

    response_tree = html.fromstring(r.content)
    flag = response_tree.xpath("/html/body/div[2]/div/div[2]/div[1]")[0]
    print(flag.text)


if __name__ == "__main__":
    main()
