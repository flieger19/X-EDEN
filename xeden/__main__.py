"""
Documentation
"""
import getopt
import sys

import xeden.toolchain.create as toolchain


def usage():
    print("usage: setup.py [-h, -t, --help, --tool]")


def main(argv=sys.argv):
    exit_code = 0

    try:
        opts, args = getopt.getopt(argv, "ht", ["help", "tool"])
    except getopt.GetoptError as error:
        # print help information and exit:
        print(error)  # will print something like "option -a not recognized"
        usage()
        exit_code = 2
        return exit_code
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            return exit_code
        elif opt in ("-t", "--tool"):
            toolchain.create()
            return exit_code
        else:
            assert False, "unhandled option"

    toolchain.create()

    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
