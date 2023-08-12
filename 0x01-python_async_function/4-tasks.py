#!/usr/bin/env python3
"""Module that shows how async python works"""

import asyncio
from typing import List
from functools import partial


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Coroutine that spawns new tasks with task_wait_random
        n times with the specified max_delay
    """
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    await asyncio.gather(*tasks)

    delays = [task.result() for task in tasks]
    return delays


if __name__ == '__main__':
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
