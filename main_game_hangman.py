from main import check_config
from utils import my_print
from utils.myLog import myLog
from src.game.hangman import HangmanGame
import getopt
import sys

verbose = False
chances = None


def usage():
    print("usage is :")
    print(" -h | --help : print this message.")
    print(" -v | --verbose : enable verbose mode.")
    print(" -c | --chances : set number of chances for game.")


def check_opt():
    global chances
    global verbose

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:v", ["help", "chances="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    chances = None
    verbose = False
    for option, value in opts:
        if option == ("-v", "--verbose"):
            verbose = True

        elif option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ("-c", "--chances"):
            chances = value
        else:
            assert False, "unhandled option"


if __name__ == "__main__":

    program = "game_hangman.py"
    # use my printer util
    p = my_print

    check_opt()

    if verbose:
        p.cout("> verbose mode enabled")

    p.cout("> starting " + program)
    my_cfg_path: str = 'config/logging.ini'
    # use my check_config util (to check the config path givens)
    check_config(my_cfg_path)
    # do_dog_stuff()
    log = myLog(my_cfg_path, program)

    log.d('debug message')
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

    game = HangmanGame(int(chances), dictionaryFile)
    game.start()
