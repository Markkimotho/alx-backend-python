#!/usr/bin/env python3
"""A Module for Async Generator"""

import asyncio
import random
from typing import List

async def async_generator() -> List[float]:
    """Coroutine than yields a 10 random numbers,
        with each being random
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
