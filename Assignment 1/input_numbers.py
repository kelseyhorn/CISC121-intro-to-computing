"""
This module provides functions that return numbers in response to prompts to
the user.

Functions:

input_float (prompt)
    Displays prompt (a message) and returns user (keyboard) input in the
    form of a floating-point number (a float). Displays an error message and
    repeats if the user enters a string that cannot be converted to a float.

input_integer (prompt)
    Displays prompt (a message) and returns user (keyboard) input in the
    form of an integer (an int). Displays an error message and
    repeats if the user enters a string that cannot be converted to an int.

input_natural (prompt, allow_zero=False)
    Displays prompt (a message) and returns user (keyboard) input in the
    form of a natural number. Displays an error message and
    repeats if the user enters a string that cannot be converted to a natural.
    The optional allow_zero argument controls whether or not 0 is to be
    accepted as a natural number. This defaults to False (i.e., 0 not allowed).

R. Linley
2019-08-30
"""

def input_float (prompt):
    """Displays prompt (a message) and returns user (keyboard) input in the
    form of a floating-point number (a float). Displays an error message and
    repeats if the user enters a string that cannot be converted to a float.
    """
    while True:
        try:
            return float(input(prompt)) # Trigger exception on non-float input.
        except ValueError:
            print("You must enter a floating-point number.")

def input_integer (prompt):
    """Displays prompt (a message) and returns user (keyboard) input in the
    form of an integer (an int). Displays an error message and
    repeats if the user enters a string that cannot be converted to an int.
    """
    while True:
        try:
            return int(input(prompt)) # Trigger exception on non-int input.
        except ValueError:
            print("You must enter an integer.")

def input_natural (prompt, allow_zero=False):
    """Displays prompt (a message) and returns user (keyboard) input in the
    form of a natural number. Displays an error message and
    repeats if the user enters a string that cannot be converted to a natural.
    The optional allow_zero argument controls whether or not 0 is to be
    accepted as a natural number. This defaults to False (i.e., 0 not allowed).
    """
    while True:
        min_val = 1 # i.e., natural numbers are 1, 2, 3, ...
        try:
            n = int(input(prompt)) # Trigger exception if n is not an int.
            if allow_zero:
                min_val = 0 # i.e., natural numbers are 0, 1, 2, 3, ...
            if n < min_val:            
                raise ValueError # Trigger exception if n not a natural int.
            return n
        except ValueError:
            print("You must enter an integer greater than or equal to "\
                  + str(min_val) + ".")
                
if __name__ == '__main__':
    # Testing!

    # Floating-point number input
    print (input_float("Enter a floating-point number: "))

    # Integer input
    print (input_integer("Enter an integer: "))

    # Natural numbers input:
    #   1, 2, 3, ...
    print (input_natural("Enter a natural number (greater than 0): "))
    #   0, 1, 2, 3, ...
    print (input_natural("Enter a natural number (greater than or "\
                         "equal to 0): ", True))
