#!/usr/bin/env python3
"""An annotated module that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that returns a function that
     multiplies a float by multiplier"""
    def multiply(value: float) -> float:
        """A multiplier function"""
        return value * multiplier

    return multiply
