#!/usr/bin/env python3
"""An annotated module that returns a tuple from string and int/float"""
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A function that returns a tuple of (args1), (args2*args2)"""
    return (k, v*v)
