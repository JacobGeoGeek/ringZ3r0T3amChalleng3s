import requests
import sys
import getpass
from bs4 import BeautifulSoup

URL_LOGIN = "https://ringzer0ctf.com/login"
URL_CHALLENGE = "https://ringzer0ctf.com/challenges/{0}"


def login():
    user_name = getpass.getuser("Enter your user name: ")
    password = getpass.getpass("Enter your password: ")

    payload = {"username": user_name, "password": password}

    result = requests.post(URL_LOGIN, data=payload)
    login_success = BeautifulSoup(result.text, "html.parser").find_all(
        "div", class_="alert alert-danger")

    if len(login_success) != 0:
        print("Error, cannot connect")
        login()

    return result.content


if __name__ == "__main__":
    login()
    print("contract you are connected")
