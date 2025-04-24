#!/usr/bin/env python3

"""Has sum_mixed_list function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Gets sum of a mixed list
    """

    sum: float = 0.0

    for number in mxd_lst:
        sum = sum + number

    return sum
