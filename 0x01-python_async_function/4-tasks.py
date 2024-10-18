#!/usr/bin/env python3
"""
4-tasks module
"""
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """new version of wait_n"""

    task_wait_random = __import__('3-tasks').task_wait_random
    delays = [task_wait_random(max_delay) for i in range(n)]
    tasks = []

    for task in asyncio.as_completed(delays):
        tasks.append(await task)

    return tasks
