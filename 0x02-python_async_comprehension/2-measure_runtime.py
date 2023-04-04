#!/usr/bin/env python3
'''Run time for four parallel comprehensions'''


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures runtime and returns an array'''
    start = time.perf_counter()
    task = [asyncio.create_task(async_comprehension()) for i in range(4)]
    result = await asyncio.gather(*task)
    end = time.perf_counter()
    total_time = end - start
    return total_time
