#!/usr/bin/env python3
'''
    Function 'sum_mixed_list'
    Takes a list 'mxd_lst' of integers and floats
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
        Returns the sum of a list of integers and floating-point numbers.
    '''
    return float(sum(mxd_lst))
