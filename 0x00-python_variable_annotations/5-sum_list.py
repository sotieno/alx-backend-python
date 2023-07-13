#!/usr/bin/env python3
'''
    Function 'sum_list' which takes a list 'input_list' of floats as argument
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
        Returns the sum of a list of floating-point numbers.
    '''
    return float(sum(input_list))
