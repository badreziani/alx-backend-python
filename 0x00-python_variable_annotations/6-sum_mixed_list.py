#!/usr/bin/env python3
"""
6-sum_mixed_list module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of floats & ints"""
    return sum(float(n) for n in mxd_lst)
