from utils import my_print
from utils.checkConfig import check_config
from utils.myLog import myLog
from src.game.hangman import HangmanGame

import time
import getopt
import sys

verbose = False
chances = 10
ask_for_name = False


def usage():
    print("usage is :")
    print(" -h | --help : print this message.")
    print(" -v | --verbose : enable verbose mode.")
    print(" -n | --name : ask for player name.")
    print(" -c | --chances : set number of chances for game.")


def check_opt():
    global chances
    global verbose
    global ask_for_name

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvnc:", ["help", "verbose", "name", "chances="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for option, value in opts:
        if option in ("-v", "--verbose"):
            verbose = True
        elif option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ("-c", "--chances"):
            chances = value
        elif option in ("-n", "--name"):
            ask_for_name = True
        else:
            assert False, "unhandled option"


def ask_player_name():
    time.sleep(0.5)
    user_name = input("C est qui ton p\'tit nom? ")
    time.sleep(0.5)
    print("OK, " + user_name, ", c est l\'heure du pendu...")
    print("")


if __name__ == "__main__":

    program = "game_hangman.py"
    # use my printer util
    p = my_print
    # check given options of program
    check_opt()

    if verbose:
        p.cout("> verbose mode enabled")

    p.cout("> starting " + program)
    my_cfg_path: str = 'config/logging.ini'
    # use my check_config util (to check the config path givens)
    check_config(my_cfg_path)

    log = myLog(my_cfg_path, program)

    # log.d('debug message')
    # log.i('info message')
    # log.w('warn message')
    # log.e('error message')
    # log.c('critical message')
    dictionaryFile = 'assets/french_words.txt'
    file = None

    try:
        file = open(dictionaryFile)
        # Do something with the file
    except IOError:
        log.e('File not accessible')
        p.cerr("File not accessible")
    finally:
        file.close()

    # ask for player name if requested
    if ask_for_name:
        ask_player_name()

    # start a hangman game with given options
    game = HangmanGame(int(chances), dictionaryFile, verbose)
    game.start()
