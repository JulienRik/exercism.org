"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(n):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument n and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    total = EXPECTED_BAKE_TIME - n
    return total


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    Parameters:
        number_of_layers (int): Number of layers for lasagna.

    Returns:
        int: The total preparation time (in minutes) derived from 'PREPARATION_TIME' per 'number_of_layers'.

    Function that takes the 'number_of_layers' and returns the 'PREPARATION_TIME' in total.
    """
    prep_time = number_of_layers * PREPARATION_TIME
    return prep_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function takes the result of preparation_time_in_minutes and elapsed_bake_time as argument and returns elapsed_time_in_minutes as result.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
