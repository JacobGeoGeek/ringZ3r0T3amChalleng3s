import requests
import challenge14

URL_CHALLENGE = "https://ringzer0ctf.com/challenges/{0}"


def solve_challenge(challenge_number: int, session: requests.Session) -> None:
    html_content = session.get(URL_CHALLENGE.format(challenge_number)).text
    if challenge_number == 14:
        hash_message = challenge14.solve_problem(html_content)
        print(URL_CHALLENGE.format(challenge_number) +
              "/{0}".format(hash_message))
        # result = session.get(URL_CHALLENGE.format(challenge_number) + "/{0}".format(hash_message))
        # print(result.text)
