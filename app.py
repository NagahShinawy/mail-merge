"""
created by Nagaj at 10/06/2021
"""
from file import File
from mail import Mail


LETTER_PATH = "./inputs/letters/starting_letter.txt"
NAMES_PATH = "./inputs/names/names.txt"
SENDING_MAIL_PATH = "./output/readyToSend"


if __name__ == "__main__":
    namef = File(path=NAMES_PATH)
    mailtemplate = File(path=LETTER_PATH).content

    for name in namef:
        body = mailtemplate.replace("[name]", name)
        new_main = Mail(recipient=name, content=body, saved_to=SENDING_MAIL_PATH)
        new_main.send()
