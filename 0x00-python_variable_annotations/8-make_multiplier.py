#!/usr/bin/env python3
"""
8-make_multiplier module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a callable"""
    return lambda x: x * multiplier
