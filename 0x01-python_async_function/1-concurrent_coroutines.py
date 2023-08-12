#!/usr/bin/env python3
"""Module that illustrates the execution of multiple coroutines
at the same time"""

import asyncio
from typing import List
from functools import partial
from itertools import repeat
from random import randint
from time import sleep


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Coroutine that spawns wait_random n times
    with the specified max_delay
    """
    delays = []

    async def process_delay():
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*[process_delay() for _ in range(n)])

    return sorted(delays)
