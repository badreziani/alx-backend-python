#!/usr/bin/env python3
"""
7-to_kv module
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple as (k, v)"""
    return (k, v**2)
