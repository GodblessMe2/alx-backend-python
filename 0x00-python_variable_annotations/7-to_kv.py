#!/usr/bin/env python3
from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v**2.0)
