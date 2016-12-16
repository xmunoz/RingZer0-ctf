import requests
from lxml import html
import os


def main():
    '''
    Solution to "Some Martian Message".
    '''
    BASE_URL = "https://ringzer0team.com/challenges/25/"
    cookie = {
        "PHPSESSID": os.getenv("PHPSESSID"),
    }
    response = requests.get(BASE_URL, cookies=cookie)
    tree = html.fromstring(response.content)
    message = tree.xpath("/html/body/div[2]/div/div[2]")[0].text
    message = message.strip()
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uppercase_reverse_lookup = {uppercase[i]:i for i in range(0,len(uppercase))}

    shift = -13
    decrypted_message = ""
    for char in message:
        if char.islower():
            char_upper = char.upper()
            decrypted_message += uppercase[uppercase_reverse_lookup[char_upper] + shift].lower()
        else:
            decrypted_message += uppercase[uppercase_reverse_lookup[char] + shift]

    print(decrypted_message)


if __name__ == "__main__":
    main()
