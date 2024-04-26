#!/usr/bin/python3
""" Task 9 """
from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """Duck type the behaviour of the function"""
    return [(i, len(i)) for i in lst]
