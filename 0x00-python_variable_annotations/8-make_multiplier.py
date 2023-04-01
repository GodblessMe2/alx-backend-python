#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function that multiplies a float by multiplier.
    '''
    def multiplier_fn(num: float) -> float:
        return num * multiplier
    return multiplier_fn
