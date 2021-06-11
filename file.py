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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.content == other.content
        if isinstance(other, str):
            return self.content == other
        self.raise_error(other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.content > other.content
        self.raise_error(other)

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.content >= other.content
        self.raise_error(other)

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.content < other.content
        self.raise_error(other)

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.content <= other.content
        self.raise_error(other)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.content + other.content
        if isinstance(other, str):
            return self.content + other
        self.raise_error(other)

    def raise_error(self, other):
        raise TypeError(
            f"can not compare '{self.__class__.__name__}' to '{other.__class__.__name__}'"
        )

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
