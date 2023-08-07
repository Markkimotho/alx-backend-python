#!/usr/bin/env python3
"""Module that measures the runtime of a function"""

import time
import asyncio
from typing import List
from random import randint
from itertools import repeat
from functools import partial


wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function that measures the total execution time for wait_n()"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == '__main__':
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
