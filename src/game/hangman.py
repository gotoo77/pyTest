import time
import random


def welcome():
    # welcoming the user
    time.sleep(0.5)
    name = input("C est qui ton p\'tit nom? ")
    print("OK, " + name, ", c est l\'heure du pendu...")
    print("")


class HangmanGame:
    def __init__(self, chances, dictionary):
        self.nbChances = chances
        self.dictionary = dictionary

    def start(self):
        # welcoming the user
        welcome()

        # read dictionary of words into list
        file = open(self.dictionary)
        # List = open(self.dictionary).readlines()
        List = file.read().splitlines()

        # set the secret
        word = random.choice(List)
        # print("random word form dictionary is: ", word)

        # creates an variable with an empty value
        guesses = ''
        previous_wrongs = ''

        while self.nbChances > 0:
            # make a counter that starts with zero
            failed = 0
            # for every character in secret_word
            for char in word:
                # see if the character is in the players guess
                if char in guesses:
                    # print then out the character
                    print(char, end=' '),

                else:
                    # if not found, print a dash
                    print("_", end=' '),
                    # and increase the failed counter with one
                    failed += 1

                    # if failed is equal to zero, print You Won
            if failed == 0:
                print("")
                print("Bravo, quel talent !")
                # exit the script
                break

            print()
            # ask the user go guess a character
            guess = ""
            while not (guess.isalpha() and len(guess) == 1):
                guess = input("propose une lettre (1 caractere alpha) :")
                guess = str(guess).lower()

            # store player's guesses
            guesses += guess
            print("historiques des essais {", end='')
            for g in guesses:
                print(g + ", ", end='')
            print("}")

            # if the guess is not found in the secret word
            if guess not in word:
                # self.nbChances counter decreases
                self.nbChances -= 1
                print("désolé, pas de '" + guess + "'!")
                previous_wrongs += guess

                print("erreurs precedents=", end='')
                for w in previous_wrongs:
                    print("'" + w + "', ", end='')
                print("")

            # how many chances are left
            print(" > Il vous reste ", + self.nbChances, 'chance(s)')

            # if the self.nbChances are equal to zero
            if self.nbChances == 0:
                print("Perdu... omg quelle tristesse!")
                print("> le mot était : " + word)
                time.sleep(1)
                print("c'était facile pourtant :)")
