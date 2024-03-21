#!/usr/bin/env python3i
"""
    Return the first element of an iterable, or None if the iterable is empty.
"""
from typing import Iterable, Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of an iterable, or None if the iterable is empty.

    Args:
        lst (Iterable[Any]): The input iterable.

    Returns:
        Union[Any, None]: The first element of the iterable, or None if the iterable is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
