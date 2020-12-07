import requests
import challenge14
import time

URL_CHALLENGE = "https://ringzer0ctf.com/challenges/{0}"


def solve_challenge(challenge_number: int, session: requests.Session) -> None:
    if challenge_number == 14:
        html_content = session.get(URL_CHALLENGE.format(challenge_number)).text
        startTime = time.perf_counter()
        hash_message = challenge14.solve_problem(html_content)
        result = session.get(
            URL_CHALLENGE.format(challenge_number) + "/{0}".format(hash_message)
        )
        endTime = time.perf_counter()
        print(f"time: {endTime-startTime:0.4f} seconds")
        print(result.text)
