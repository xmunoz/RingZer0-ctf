import requests
from lxml import html
import hashlib
import binascii
import os


def main():
    '''
    Solution to "I hate mathematics".
    Requires that you set an environment variable PHPSESSID.
    '''
    BASE_URL = "https://ringzer0team.com/challenges/32/"
    cookie = {
        "PHPSESSID": os.getenv("PHPSESSID"),
    }

    response = requests.get(BASE_URL, cookies=cookie)   
    tree = html.fromstring(response.content)
    message = tree.xpath("/html/body/div[2]/div/div[2]/div/text()[2]")[0]
    message = message.strip()
    parts = message.split()

    num1 = int(parts[0]) # already a base 10 number
    num2 = int(parts[2], 16) # convert hex number (0x25df) to base 10
    num3 = int('0b' + parts[4], 2) # convert binary number (110011100001) to base 10
    equation = [str(num1), parts[1], str(num2), parts[3], str(num3)]
    result = eval("".join(equation))

    url = BASE_URL + str(result)
    r = requests.get(url, cookies=cookie)

    response_tree = html.fromstring(r.content)
    flag = response_tree.xpath("/html/body/div[2]/div/div[2]/div[1]")[0]
    print(flag.text)


if __name__ == "__main__":
    main()
