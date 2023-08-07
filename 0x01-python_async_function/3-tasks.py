#!/usr/bin/env python3
"""Module that shows how async python runs"""

import asyncio
from typing import Any
from functools import partial


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """Function that takes an integer max_delay and returns a asyncio.Task"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task


if __name__ == '__main__':
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
