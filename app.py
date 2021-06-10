"""
created by Nagaj at 10/06/2021
"""
from file import File
from mail import Mail


LETTER_PATH = "./inputs/letters/starting_letter.txt"
NAMES_PATH = "./inputs/names/names.txt"
SENDING_MAIL_PATH = "./output/readyToSend"


if __name__ == "__main__":
    namesf = File(path=NAMES_PATH)
    mailtemplate = File(path=LETTER_PATH).content

    for name in namesf:
        body = mailtemplate.replace("[name]", name)
        mail = Mail(recipient=name, content=body, saved_to=SENDING_MAIL_PATH)
        mail.send()
