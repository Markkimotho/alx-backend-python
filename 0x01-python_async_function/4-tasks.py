#!/usr/bin/env python3
"""Module that shows how async python works"""
import asyncio
from typing import List, Any
from random import randint
from itertools import repeat
from functools import partial


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function similar to that in task 3
    but task_wait_random is being called
    """
    tasks = [task_wait_random(max_delay) for _ in repeat(None, n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays, key=lambda x: randint(0, max_delay))


if __name__ == '__main__':
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
