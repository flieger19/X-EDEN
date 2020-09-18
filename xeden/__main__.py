"""
Documentation
"""
import getopt
import sys


def main(argv=sys.argv):
    exit_code = 0

    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
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

    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
