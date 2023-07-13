#!/usr/bin/env python3
'''
    Function 'make_multiplier'
    Takes a float multiplier as argument
    Returns a function that multiplies a float by multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
        Creates a multiplier function.
    '''
    return lambda x: x * multiplier
