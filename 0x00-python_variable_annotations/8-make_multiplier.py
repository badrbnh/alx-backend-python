#!/usr/bin/env python3
'''make_multiplier function'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier.'''
    def mult(x: float) -> float:
        '''returns a float multiplied with multiplier'''
        return x * multiplier
    return mult
