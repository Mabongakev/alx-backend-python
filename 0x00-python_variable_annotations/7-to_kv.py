#!/usr/bin/env python3

"""Has to_kv function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of a str and a [int | float]

    Args:
        k (str): a string
        v (int, float): int or float

    Returns:
        a tuple
    """

    return (k, v * v)
