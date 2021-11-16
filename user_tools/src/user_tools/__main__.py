""" user tools app """     # Adding docstring module #
# Password Generator #
import random

if __name__ == "__main__":      # Indentation is Curly Braces for Python

    password_length = int(input("Please enter a Password Length: "))
    #print(type(password_length))   # Prints type of variable
    print("Password Length: " + str(password_length))

    char_pool = []          # List datatype

    for char_code in range(ord('A'), ord('Z') + 1): # ord returns Unicode number for a character
        char_pool.append(chr(char_code))    # List is created having all characters from A to Z

    for char_code in range(ord('a'), ord('z') + 1):
        char_pool.append(chr(char_code))    # Adding a to z to char_pool list

    for char_code in range(ord('0'), ord('9') + 1):
        char_pool.append(chr(char_code))    # Adding 0 to 9 to char_pool list

    generated_password = []

    for _ in range(password_length):
        char_pool_index  = random.randrange(0,len(char_pool)) #Range value goes upto len - 1
        generated_password.append(char_pool[char_pool_index]) # Each generated char stored in generated_password

    print("".join(generated_password))  # Another way of concat each character var
