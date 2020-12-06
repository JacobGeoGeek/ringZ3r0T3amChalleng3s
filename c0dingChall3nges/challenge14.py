from bs4 import BeautifulSoup
import re
import hashlib


def solve_problem(html_content: str):
    message = BeautifulSoup(html_content, "html.parser").find(
        class_="message").text
    message = re.sub(r'[^01]', '', message)
    return hashlib.sha512(message.encode()).hexdigest()
