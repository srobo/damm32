"""Utility functions for the tests."""

import random
from typing import List

ALPHABET = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
]


def random_string(length: int, alphabet: List[str] = ALPHABET) -> str:
    """
    Get a string of random length.

    :param length: Length of string.
    :param alphabet: alphabet to use in string.
    :returns: Random string
    """
    return "".join([random.choice(alphabet) for _ in range(length)])
