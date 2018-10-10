"""This file contains checksum implementations."""

from typing import List

Digit = int
DigitList = List[Digit]
Alphabet = List[str]


class BadCharacterException(ValueError):
    """An invalid character was found in your input."""

    pass


class BadAlphabetException(Exception):
    """That alphabet is of the wrong length or has duplicate characters."""

    pass


class Damm32:
    """Implementation of the Damm algorithm."""

    BASE_SIZE = 32
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7']  # noqa: E501

    def __init__(self, alphabet: Alphabet = ALPHABET) -> None:
        if len(set(alphabet)) != 32 or len(alphabet) != 32:
            raise BadAlphabetException

    def _calculate_from_digits(self, digits: DigitList) -> Digit:
        mask = 37
        checkdigit = 0
        for digit in digits:
            checkdigit ^= digit
            checkdigit <<= 1
            if checkdigit >= Damm32.BASE_SIZE:
                checkdigit ^= mask
        return checkdigit

    def _to_digits(self, word: str) -> DigitList:
        if type(word) is not str:
            raise TypeError
        word = word.upper()
        try:
            dl = []
            for i in word:
                dl.append(Damm32.ALPHABET.index(i))
            return dl
        except ValueError:
            pass
        raise BadCharacterException

    def _to_word(self, digits: DigitList) -> str:
        word = ""
        for i in digits:
            word += Damm32.ALPHABET[i]
        return word

    def calculate(self, word: str) -> str:
        """Calculate the check digit for a string."""
        digits = self._to_digits(word)
        checkdigit = self._calculate_from_digits(digits)
        return Damm32.ALPHABET[checkdigit]

    def verify(self, word: str) -> bool:
        """Verify that a string contains a valid check digit."""
        return self.calculate(word) == Damm32.ALPHABET[0]
