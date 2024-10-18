#!/usr/bin/env python3
"""
2-measure_runtime module
"""
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n
    """

    wait_n = __import__('1-concurrent_coroutines').wait_n

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    return (end_time - start_time) / n
