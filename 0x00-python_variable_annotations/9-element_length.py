#!/usr/bin/env python3
"""
9-element_length module
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Retruns a list of tuples"""
    return [(i, len(i)) for i in lst]
