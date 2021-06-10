"""
created by Nagaj at 10/06/2021
"""


class File:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"File <{self.path}>"

    def __getitem__(self, item):
        return self.lines[item]

    @property
    def content(self):
        with open(self.path, "r") as fin:
            return fin.read()

    @property
    def lines(self):
        with open(self.path) as fin:
            return [name.strip() for name in fin.readlines()]

    def write(self, content):
        with open(self.path, "w") as fout:
            fout.write(content)
