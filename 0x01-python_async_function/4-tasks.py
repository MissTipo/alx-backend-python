#!/usr/bin/env python3
"""Executeis multiple coroutines at the same time with async"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes in 2 int arguments and return the list of all the delays in
    ascending order
    """
    delay_tasks: List[float] = []
    for i in range(n):
        delay_tasks.append(await task_wait_random(max_delay))
    return sorted(delay_tasks)
