""" user tools app """     # Adding docstring module #

import random

if __name__ == "__main__":      # Indentation is Curly Braces for Python

    password_length = int(input("Please enter a Password Length: "))
    #print(type(password_length))   # Prints type of variable
    print("Password Length: " + str(password_length))

    char_pool = []

    char_pool.append('A')
    char_pool.append('B')
    char_pool.append('C')
    char_pool.append('1')
    char_pool.append('2')
    char_pool.append('3')

    print(len(char_pool))       # Length/size of char_pool
    print(char_pool)            # Prints contents of char_pool
    print(",".join(char_pool))  # Prints out data with "," in between
