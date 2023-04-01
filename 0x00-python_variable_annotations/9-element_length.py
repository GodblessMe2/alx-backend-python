#!/usr/bin/env python3
'''Task 9's module.
'''
from typing import Iterable, List, Sequence, Tuple
'''Retrieves the values with the appropriate types.
'''

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
