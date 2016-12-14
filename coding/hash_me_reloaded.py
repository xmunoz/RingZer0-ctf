import requests
from lxml import html
import hashlib
import binascii
import os


def main():
    '''
    Solution to "Hash me reloaded".
    Requires that you set an environment variable PHPSESSID.
    '''
    BASE_URL = "https://ringzer0team.com/challenges/14/"
    cookie = {
        "PHPSESSID": os.getenv("PHPSESSID"),
    }
    response = requests.get(BASE_URL, cookies=cookie)
    tree = html.fromstring(response.content)
    message = tree.xpath("/html/body/div[2]/div/div[2]/div/text()[2]")[0]
    message = message.strip()

    n = int('0b' + message, 2)
    decoded_message = binascii.unhexlify('%x' % n)
    result = hashlib.sha512(decoded_message).hexdigest()
    url = BASE_URL + result
    r = requests.get(url, cookies=cookie)

    response_tree = html.fromstring(r.content)
    flag = response_tree.xpath("/html/body/div[2]/div/div[2]/div[1]")[0]
    print(flag.text)


if __name__ == "__main__":
    main()
