#!/usr/bin/env python3
'''
    Creates a measure_time function with integers n and max_delay as arguments.
    The function measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. The function returns a float.
    I make use of the time module to measure an approximate elapsed time.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
        Computes the average runtime of wait_n.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
