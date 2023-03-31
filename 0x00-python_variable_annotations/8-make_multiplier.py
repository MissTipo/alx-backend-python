#!/usr/bin/env python3
'''Complex types - functions'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multipliers(n: float) -> float:
        return n * multiplier
    return multipliers
