from __future__ import print_function
import sys


def err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def ok(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)
