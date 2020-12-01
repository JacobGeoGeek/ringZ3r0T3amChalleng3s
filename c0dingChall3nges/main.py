import requests
import sys
import getpass


URL_LOGIN = "https://ringzer0ctf.com/login"
URL_CHALLENGE = "https://ringzer0ctf.com/challenges/{0}"


def login():
    user_name = getpass.getuser("Enter your user name: ")
    password = getpass.getpass("Enter your password: ")

    payload = {"username": user_name, "password": password}

    result = requests.post(URL_LOGIN, payload)

    if not result.ok:
        print("Error cannot connect")
        login()

    return result.content


if __name__ == "__main__":
    login()
