#!/usr/bin/python3
""" Task 7 """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    def mul_function(number: float) -> float:
        """returns the multiplication"""
        return number * multiplier
    return mul_function
