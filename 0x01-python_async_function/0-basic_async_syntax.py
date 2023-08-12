#!/usr/bin/env python3
"""Module that shows a basic async process"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function that waits for random delay before exec"""
    random_time = random.uniform(0, max_delay)
    await asyncio.sleep(random_time)
    return random_time
