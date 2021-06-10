"""
created by Nagaj at 10/06/2021
"""
import os
NOTIFICATION = "MAIL SENT TO '{name}'"


class Mail:
    def __init__(self, recipient, content, saved_to):
        self.recipient = recipient
        self.content = content
        self.saved_to = saved_to

    def send(self):
        mailpath = os.path.join(self.saved_to, f"letter_for_{self.recipient}.txt")
        with open(mailpath, "w") as fout:
            fout.write(self.content)
        print(NOTIFICATION.format(name=self.recipient))
