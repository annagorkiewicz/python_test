from typing import Union


def divide(dividend: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError('Divisor can not be zero.')

    return dividend / divisor


def multiply(*args: Union[int, float]):
    if len(args) == 0:
        raise ValueError('At least one value must be provided.')

    total = 1
    for arg in args:
        total *= arg

    return total
