#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable
'''returns a function that multiplies a float by multiplier.
    '''


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_fn(num: float) -> float:
        return num * multiplier
    return multiplier_fn
