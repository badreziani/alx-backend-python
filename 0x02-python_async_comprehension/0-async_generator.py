#!/usr/bin/env python3
"""
0-async_generator module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    yields a random number between 0 and 10.
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
