#!/usr/bin/env python3
"""An annotated module of its function parameters"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function that returns annotations of its arguments"""

    return [(i, len(i)) for i in lst]
