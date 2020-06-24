from utils import my_print


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each dog
        self.p = my_print

    def add_trick(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        self.p.ok(self.name + " tricks are : ")
        self.p.ok(self.tricks)

