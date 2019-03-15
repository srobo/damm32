"""Test that the class is able to verify an alphabet is valid."""

import pytest
from damm32 import Damm32
from damm32.checksum import BadAlphabetException, BadCharacterException


def test_default_alphabet():
    """Test that the default alphabet does not throw an error."""
    Damm32()


def test_empty_alphabet():
    """Test that an empty alphabet does throw an error."""
    with pytest.raises(BadAlphabetException):
        Damm32([])


def test_valid_alphabet():
    """Test that a valid alphabet does not throw an error."""
    alphabet = [
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
    Damm32(alphabet)


def test_short_alphabet():
    """Test that a short alphabet does throw an error."""
    alphabet = [
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
    ]
    with pytest.raises(BadAlphabetException):
        Damm32(alphabet)


def test_long_alphabet():
    """Test that a long alphabet does throw an error."""
    alphabet = [
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
        "?",
        "@",
        "=",
    ]
    with pytest.raises(BadAlphabetException):
        Damm32(alphabet)


def test_duplicate_alphabet():
    """Test that an alphabet with duplicates does throw an error."""
    alphabet = [
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
        "6",
    ]
    with pytest.raises(BadAlphabetException):
        Damm32(alphabet)


def test_bad_letter_detected():
    """Test that a bad letter throws an error."""
    with pytest.raises(BadCharacterException):
        d32 = Damm32()
        d32.calculate("?@")
