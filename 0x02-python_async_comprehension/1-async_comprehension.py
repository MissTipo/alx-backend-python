#!/usr/bin/env python3
'''Async Comprehensions'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    A coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers
    '''
    random_num = [random_int async for random_int in async_generator()]
    return random_num
