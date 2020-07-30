from utils import my_print


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each dog
        self.p = my_print

    def remove_trick(self, trick):
        """remove_trick : method used to remove a trick from the list of tricks
        (if trick search is already in list, if not, nothing done)
        """
        if trick in self.tricks:
            self.tricks.remove(trick)
        else:
            "done nothing : can't remove cause not found :)"

    def add_trick(self, trick):
        """add_trick : method used to add a new trick to existing list of tricks"""
        self.tricks.append(trick)

    def show_tricks(self):
        self.p.cout(self.name + " tricks are : ")
        self.p.cout(self.tricks)

