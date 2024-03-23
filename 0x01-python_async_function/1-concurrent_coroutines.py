#!/usr/bin/env python3
"""
    Asynchronous routine that spawns wait_random n
    times with the specified max_delay.
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Asynchronous routine that spawns wait_random n
        times with the specified max_delay.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
