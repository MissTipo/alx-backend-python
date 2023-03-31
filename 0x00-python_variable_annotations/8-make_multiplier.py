#!/usr/bin/env python3
'''Complex types - functions'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    that takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier
    '''
    def multipliers(n: float) -> float:
        '''multiplies a float by multiplier'''
        return n * multiplier
    return multipliers
