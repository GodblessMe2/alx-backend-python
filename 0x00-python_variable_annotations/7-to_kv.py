#!/usr/bin/env python3
'''Task 7's module.
'''
from typing import Union
from typing import Tuple
'''Converts a key and its value to a tuple of the key and
    the square of its value.
'''


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v**2.0)
