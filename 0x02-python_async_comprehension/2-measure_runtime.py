#!/usr/bin/env python3
"""A Module that measure the Runtime for four parallel comprehensions"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that runs async_comprehension 4 times in parallel
    using asyncio.gather and measures its runtime.

    Returns:
        float: Total runtime of executing async_comprehension
        4 times in parallel.
    """
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
