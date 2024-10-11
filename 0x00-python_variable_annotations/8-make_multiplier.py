#!/usr/bin/env python3
"""
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a callable"""
    return lambda x: x * multiplier
