#!/usr/bin/env python3
"""
    Asynchronous function that spawns tasks for wait_random
    n times with the specified max_delay.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that spawns tasks for wait_random
    n times with the specified max_delay.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
