#!/usr/bin/env python3
""" Coroutine to measure the total runtime of executing
    async_comprehension four times in parallel.
"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension
import time


async def measure_runtime() -> float:
    """ Coroutine to measure the total runtime of executing
    async_comprehension four times in parallel.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
