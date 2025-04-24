#!/usr/bin/env python3

"""Has make_multiplier function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a multiplier

    Args:
        multiplier (float): a float

    Returns:
        function that multiplies
    """

    def func(number: float) -> float:
        return number * multiplier

    return func
