""" parse command-line arguments """

from argparse import ArgumentParser,Namespace

def get_args() -> Namespace:
    """ parse and return command-line arguments """
    # Add argument when invoking the program #
    parser = ArgumentParser()

    # Positional Argument: main.py 20 #
    parser.add_argument("password_length",
    type=int,
    help="Length of Password")

    # Keyword Arguments for additional arguments : main.py -xl 20 #
    parser.add_argument(
        "-xn",
        "--exclude-numbers",
        action="store_true",
        help="Do not include numbers in generated password"
    )

    parser.add_argument(
        "-xl",
        "--exclude-letters",
        action="store_true",
        help="Do not include letters in generated password"
    )

    parser.add_argument(
        "-xlc",
        "--exclude-lowercase-letters",
        action="store_true",
        help="Do not include lowercase letters in generated password"
    )

    parser.add_argument(
        "-xuc",
        "--exclude-uppercase-letters",
        action="store_true",
        help="Do not include uppercase letters in generated password"
    )

    parser.add_argument(
        "-xs",
        "--exclude-symbols",
        action="store_true",
        help="Do not include symbols in generated password"
    )

    return parser.parse_args()
