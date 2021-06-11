"""
created by Nagaj at 10/06/2021
"""
from file import File
from mail import Mail


LETTER_PATH = "./inputs/letters/starting_letter.txt"
NAMES_PATH = "./inputs/names/names.txt"
SENDING_MAIL_PATH = "./output/readyToSend"
PLACEHOLDER = "[name]"

if __name__ == "__main__":
    recipients = File(path=NAMES_PATH)
    letter = File(path=LETTER_PATH).content

    for recipient in recipients:
        body = letter.replace(PLACEHOLDER, recipient)
        mail = Mail(recipient=recipient, content=body, saved_to=SENDING_MAIL_PATH)
        mail.send()
