""" parse command-line arguments """

from argparse import ArgumentParser,Namespace

def get_args() -> Namespace:
    """ parse and return command-line arguments """
    # Add argument when invoking the program #
    parser = ArgumentParser()
    parser.add_argument("password_length", type=int, help="Length of Password")

    return parser.parse_args()
