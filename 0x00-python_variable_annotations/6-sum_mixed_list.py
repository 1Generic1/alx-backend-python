#!/usr/bin/env python3
"""Returns the sum of floats in a list."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of floats in a list."""
    return float(sum(mxd_lst))
