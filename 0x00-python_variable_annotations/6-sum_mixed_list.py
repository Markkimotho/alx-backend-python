#!/usr/bin/env python3
"""An annotated module that returns the sum of a list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A function that returns the sum of a list's elements
    given a mix of ints and floats as their arguments"""
    return sum(mxd_lst)
