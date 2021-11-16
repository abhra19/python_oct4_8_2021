""" user tools app """     # Adding docstring module #
# Password Generator #
# Check the options available : main.py --help #
import random
from user_tools.args import get_args

def append_chars_to_pool(
    first_letter: str,
    last_letter: str,
    pool: list[str]) -> None:
    """ append chars to the char pool """

    for code in range(ord(first_letter), ord(last_letter) + 1):
        pool.append(chr(code))

if __name__ == "__main__":      # Indentation is Curly Braces for Python

    args=get_args()
    print("Password Length: " + str(args.password_length))
    char_pool: list[str] = []          # List datatype

    if not args.exclude_numbers:
        append_chars_to_pool('0','9',char_pool)

    if not args.exclude_letters and not args.exclude_uppercase_letters:
        append_chars_to_pool('A','Z',char_pool)    

    if not args.exclude_letters or not args.exclude_lowercase_letters:
        append_chars_to_pool('a','z',char_pool)

    if not args.exclude_symbols:
        char_pool.append('_')
        char_pool.append('-')
        char_pool.append('%')
        char_pool.append('$')
        char_pool.append('#')
        char_pool.append('@')

    generated_password = []

    for _ in range(args.password_length):
        #Range value goes upto len - 1
        char_pool_index  = random.randrange(0,len(char_pool))
        # Each generated char stored in generated_password
        generated_password.append(char_pool[char_pool_index])

    # Another way of concat each character var
    print("".join(generated_password))
