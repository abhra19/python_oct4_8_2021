""" user tools app """     # Adding docstring module #
# Password Generator #
import random
import argparse
def append_chars_to_pool(
    first_letter: str,
    last_letter: str,
    pool: list[str]) -> None:
    """ append chars to the char pool """

    for code in range(ord(first_letter), ord(last_letter) + 1):
        pool.append(chr(code))

if __name__ == "__main__":      # Indentation is Curly Braces for Python
    # Add argument when invoking the program #
    parser = argparse.ArgumentParser()
    parser.add_argument("password_length", type=int, help="Length of Password")

    args = parser.parse_args()

    print("Password Length: " + str(args.password_length))
    char_pool: list[str] = []          # List datatype

    append_chars_to_pool('0','9',char_pool)
    append_chars_to_pool('A','Z',char_pool)
    append_chars_to_pool('a','z',char_pool)

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
