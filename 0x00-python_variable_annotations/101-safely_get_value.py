#!/usr/bin/env python3
""" This function retrieves a value associated with
a specified key from a dictionary."""

from typing import Mapping, Any, TypeVar, Optional
V = TypeVar('V')


def safely_get_value(
    dct: Mapping[Any, V],
    key: Any,
    default: Optional[V] = None
) -> V:
    """ This function retrieves a value associated with
    a specified key from a dictionary."""

    if Key in dct:
        return dct[key]
    else:
        return default
