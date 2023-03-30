#!/usr/bin/env python3
from typing import Any


def safely_get_value(dct: dict, key: str, default: Any = None) -> Any:
    if key in dct:
        return dct[key]
    else:
        return default
