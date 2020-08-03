import re
import random
import time


from utils.printList import my_list_print


class HangmanGame:
    def __init__(self, chances, dictionary,verbose):
        self.nbChances = chances
        self.dictionary = dictionary
        self.verbose = verbose

    def start(self):
        # read dictionary of words into list
        file = open(self.dictionary)
        # create liste of words using splitlines method prevent extra \n char at the end
        # List = open(self.dictionary).readlines()
        list_of_words_from_dico = file.read().splitlines()
        if self.verbose:
            print('loaded dictionary contains ' + str(list_of_words_from_dico.__len__()) + " words")

        # set the secret
        word = random.choice(list_of_words_from_dico)

        # creates an variable with an empty value
        user_guesses = ''
        previous_wrongs = ''

        while self.nbChances > 0:
            # count number of mismatched characters in the secret_word to guess
            nb_mismatch_char = 0
            # for every character in secret_word
            for char in word:
                if char in user_guesses:
                    # found the character, print it
                    print(char, end=' '),

                else:
                    charNotFound = '_'
                    # if not found, print
                    print(charNotFound, end=' '),
                    # and increase the failed counter with one
                    nb_mismatch_char += 1

            if nb_mismatch_char == 0:
                print("")
                print("Bravo, quel talent !")
                # exit the script
                break

            print()
            # ask the user go guess a character
            user_guess = ""
            while not (user_guess.isalpha()
                       and re.match("^[a-z]+$", user_guess)
                       and len(user_guess) == 1):
                user_guess = input("propose une lettre (1 caractere alpha) :")
                user_guess = str(user_guess).lower()

            # store player's guesses
            user_guesses += user_guess

            my_list_print(user_guesses, "historiques des essais")

            # if the guess is not found in the secret word
            if user_guess not in word:
                # decreasing counter or remaining chances
                self.nbChances -= 1
                print("désolé, pas de '" + user_guess + "'!")
                previous_wrongs += user_guess

                my_list_print(previous_wrongs, "erreurs precedentes")

            # how many chances are left
            print(" > Il vous reste ", + self.nbChances, 'chance(s)')

            # if the self.nbChances are equal to zero
            if self.nbChances == 0:
                print("Perdu... omg quelle tristesse!")
                print("> le mot était : " + word)
                time.sleep(1)
                print("c'était facile pourtant :)")
