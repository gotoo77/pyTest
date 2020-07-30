from __future__ import print_function
import sys


def cerr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def cout(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)
