#!/usr/bin/env python3
"""
    Coroutine that collects 10 random numbers using
    async comprehension over async_generator.
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers using
    async comprehension over async_generator.
    """
    random_numbers = [num async for num in async_generator()]
    return random_numbers
