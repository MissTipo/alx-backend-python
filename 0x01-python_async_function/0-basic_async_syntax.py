#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
     Asynchronous coroutine that waits for a random delay between 0 and
     `max_delay` seconds (inclusive) and eventually returns the delay time.

    Args:
        max_delay (float): Maximum delay time in seconds (inclusive).
        Defaults to 10.

    Returns:
        float: The delay time in seconds.
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
