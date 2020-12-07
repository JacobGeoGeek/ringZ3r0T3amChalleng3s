from bs4 import BeautifulSoup
import re


def solve_problem(html_content: str):
    message = BeautifulSoup(html_content, "html.parser").find(class_="message").text
    message = re.sub(r"[\r\t\n]", "", message)
    message = message.replace("----- BEGIN MESSAGE -----", "")
    message = message.replace("----- END MESSAGE -----", "")
    numbers = re.split("\+|\-|\*|\/|\=", message)
    return int(numbers[0]) + int(numbers[1], 16) - int(numbers[2], 2)
