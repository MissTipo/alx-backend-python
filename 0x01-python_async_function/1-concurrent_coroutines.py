#!/usr/bin/env python3
"""Executeis multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay=10) -> List[float]:
    """
    Takes in 2 int arguments and return the list of all the delays in
    ascending order
    """
    delay_tasks: List[float] = []
    for i in range(n):
        delay_tasks.append(await wait_random(max_delay))
    return delay_tasks
