#!/usr/bin/env python3
"""A Module that handle Async Comprehensions"""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Coroutine that does random number generation using
        async comprehensions perfomed on async generator
    """
    random_numbers = [num async for num in async_generator()]
    return random_numbers
