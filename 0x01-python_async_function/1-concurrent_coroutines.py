#!/usr/bin/env python3
"""
1-concurrent_coroutines module
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    """

    wait_random = __import__('0-basic_async_syntax').wait_random
    delay_list = [wait_random(max_delay) for i in range(n)]
    tasks = []

    for task in asyncio.as_completed(delay_list):
        tasks.append(await task)

    return tasks
