#!/usr/bin/env python3
'''to_kv function'''
from typing import Tuple, Union
from math import sqrt


def to_kv(k: str, v: Union[str, float]) -> Tuple[str, float]:
    '''function to_kv that takes a string k and
    an int OR float v as arguments and returns a tuple. '''
    return (k, sqrt(v))
