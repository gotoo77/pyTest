import getopt
import sys
import time

watch_period = 2
continue_loop = True


def watch_prog_return(to_watch):
    global continue_loop
    with open(to_watch) as f:
        for line in f:
            if '139' in line:
                print('\n[' + time.ctime() + "] Read ret code '" + line + "' > SEGFAULT detected!")
                continue_loop = False
                break


def usage():
    print(">> Possible options/arguments for this program are 'hw:v'\n"
          " -h = help\n"
          " -w = path of the file to watch (containing return code of program to watch)\n"
          " -v = verbose mode\n"
          )


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hw:v", ["help", "watch="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    fileToWatch = "/tmp/dtws_out_CSTEOM.txt"
    verbose = False
    for w, a in opts:
        if w == "-v":
            verbose = True
        elif w in ("-h", "--help"):
            usage()
            sys.exit()
        elif w in ("-w", "--watch"):
            fileToWatch = a
        else:
            assert False, "unhandled option"

    print('[' + time.ctime() + ']>>> Start watching (' + fileToWatch + ') <<<')
    if verbose:
        print("verbose mode is ON")
    else:
        print("verbose mode is OFF")

    while continue_loop:
        if verbose:
            sys.stdout.write('d')
        watch_prog_return(fileToWatch)
        time.sleep(watch_period)

    print('[' + time.ctime() + ']>>> End of watching (' + fileToWatch + ') <<<')


if __name__ == "__main__":
    main()
