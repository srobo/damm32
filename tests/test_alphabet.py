"""Test that the class is able to verify an alphabet is valid."""

import pytest

from damm32 import Damm32
from damm32.checksum import BadAlphabetException, BadCharacterException


def test_default_alphabet() -> None:
    """Test that the default alphabet does not throw an error."""
    Damm32()


def test_empty_alphabet() -> None:
    """Test that an empty alphabet does throw an error."""
    with pytest.raises(BadAlphabetException):
        Damm32([])


def test_valid_alphabet() -> None:
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


def test_short_alphabet() -> None:
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


def test_long_alphabet() -> None:
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


def test_duplicate_alphabet() -> None:
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


def test_bad_letter_detected() -> None:
    """Test that a bad letter throws an error."""
    with pytest.raises(BadCharacterException):
        d32 = Damm32()
        d32.calculate("?@")


def test_bad_letter_in_alphabet() -> None:
    """Test that a bad letter in the alphabet does throw an error."""
    alphabet = [
        "AAAAA",
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
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "?",
        "@",
    ]
    with pytest.raises(BadCharacterException):
        Damm32(alphabet)


def test_to_word() -> None:
    """Test that the _to_word function works."""
    d32 = Damm32()
    digit_list = [1, 2, 3, 4, 5, 1, 3, 1, 3, 3, 9, 15, 31]
    assert d32._to_word(digit_list) == "BCDEFBDBDDJP7"
    assert type(d32._to_word(digit_list)) is str


def test_to_word_non_standard_alphabet() -> None:
    """Test that the _to_word function works."""
    d32 = Damm32(list("BACDEFGHIJKLMNOPQSTUVWXYZ1234567"))
    digit_list = [1, 2, 3, 4, 5, 1, 3, 1, 3, 3, 9, 15, 31]
    assert d32._to_word(digit_list) == "ACDEFADADDJP7"
    assert type(d32._to_word(digit_list)) is str
