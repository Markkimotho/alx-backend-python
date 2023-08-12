#!/usr/bin/env python3
"""Module that illustrates the execution of multiple coroutines
at the same time"""

import asyncio
from typing import List
from random import randint
from itertools import repeat
from functools import partial


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that executes multiple coroutines with async"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*coroutines) 
