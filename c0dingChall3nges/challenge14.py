from bs4 import BeautifulSoup
import re
import hashlib
import binascii


def solve_problem(html_content: str):
    message = BeautifulSoup(html_content, "html.parser").find(class_="message").text
    message = re.sub(r"[^01]", "", message)
    intergerBase2 = int(message, 2)
    sha512 = binascii.unhexlify("%x" % intergerBase2)
    hashMessage = hashlib.sha512()
    hashMessage.update(sha512)
    return hashMessage.hexdigest()
