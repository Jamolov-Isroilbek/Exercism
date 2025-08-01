"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 6

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers for lasagna.
    :return: int - preparation time required for each layer (which takes 2 minutes per layer).

    Function that takes number of layers of lasagna and returns how much time is required for the     preparation aggregated, calculating 2 minutes per layer.
    """
    
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers: int, elapsed_time: int) -> int:
    """Calculate the elapsed time in minutes.

    :param number_of_layers: int - number of layers for lasagna.
    :param elapsed_time: int - number of minutes elapsed for lasagna to be ready
    :return: int - elapsed time in minutes by adding time that takes for layers and elapsed time      so far.

    Function that takes the number of layers and elapsed time so far, and returns the total by        summing their time together.
    """
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_time