#!/usr/bin/python3
import sys


def print_args(argc, argv):
    argc = len(argv) - 1

    if argc == 1:
        print("{} argument:".format(argc))
    elif argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} arguments:".format(argc))

    for i in range(1, (argc + 1)):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    print_args(len(sys.argv) - 1, sys.argv)
