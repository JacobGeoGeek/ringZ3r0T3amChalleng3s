import requests
import getpass
from bs4 import BeautifulSoup
import challengeManager

URL_LOGIN = "https://ringzer0ctf.com/login"


def login():
    session: requests.Session = requests.Session()
    user_name: str = input("Enter your user name: ")
    password: str = getpass.getpass("Enter your password: ")

    payload = {"username": user_name, "password": password}

    result = session.post(URL_LOGIN, data=payload)
    login_success = BeautifulSoup(result.text, "html.parser").find_all(
        "div", class_="alert alert-danger")

    if len(login_success) != 0:
        print("Error, Unable to log, please try again")
        login()

    return session


if __name__ == "__main__":
    session = login()
    challenge_number = int(input("challenge number to solve: "))
    challengeManager.solve_challenge(challenge_number, session)
