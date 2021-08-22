"""This file contains checksum implementations."""

from typing import List


class BadCharacterException(ValueError):
    """An invalid character was found in your input."""


class BadAlphabetException(Exception):
    """There was a problem with the provided alphabet."""


class Damm32:
    """Implementation of the Damm algorithm."""

    BASE_SIZE = 32
    BIT_MASK = 37  # Bitmask from Table of Low-Weight Binary Irreducible Polynomials
    _DEFAULT_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7']  # noqa: E501

    def __init__(self, alphabet: List[str] = _DEFAULT_ALPHABET) -> None:
        self._alphabet = alphabet
        self._check_alphabet_valid()

    def calculate(self, word: str) -> str:
        """
        Calculate the Damm check digit for a string.

        The string must consist only of characters in the alphabet.

        :param word: String to calculatee Damm check digit for.
        :returns: Single check digit character.
        """
        digits = self._to_digits(word)
        checkdigit = self._calculate_from_digits(digits)
        return self._alphabet[checkdigit]

    def verify(self, word: str) -> bool:
        """
        Verify that a string contains a valid Damm check digit.

        :param word: Word to check validity.
        :returns: Result of the check.
        """
        return self.calculate(word) == self._alphabet[0]

    def _check_alphabet_valid(self) -> None:
        """
        Check that the alphabet is valid.

        :raises BadAlphabetException: The alphabet was invalid.
        :raises BadCharacterException: At least one character in the alphabet is invalid.
        """
        length = len(self._alphabet)
        if length != self.BASE_SIZE:
            raise BadAlphabetException(
                f"Expected alphabet of length {self.BASE_SIZE}, got {length}",
            )

        length_unique = len(set(self._alphabet))
        if length_unique != self.BASE_SIZE:
            raise BadAlphabetException(
                f"Expected {self.BASE_SIZE} unique characters in "
                f"alphabet, got {length_unique }",
            )

        if not all(len(i) == 1 for i in self._alphabet):
            raise BadCharacterException(
                "Some characters in the provided alphabet were too long.",
            )

    def _calculate_from_digits(self, digits: List[int]) -> int:
        """
        Calculate the Damm check digit from a list of integer digits.

        :param digits: digits to calculate check digit from.
        :returns: The Damm check digit.
        """
        checkdigit = 0
        for digit in digits:
            checkdigit ^= digit
            checkdigit <<= 1
            if checkdigit >= self.BASE_SIZE:
                checkdigit ^= self.BIT_MASK
        return checkdigit

    def _to_digits(self, word: str) -> List[int]:
        """
        Convert a string to a list of integer digits.

        :param word: Word to convert.
        :returns: List of integer digits.
        :raises TypeError: Input is not a string.
        :raises BadCharacterException: Word contains an invalid character.
        """
        if type(word) is not str:
            raise TypeError("Input is not a string.")
        word = word.upper()
        try:
            return [self._alphabet.index(letter) for letter in word]
        except ValueError:
            raise BadCharacterException(f"Invalid character in {word}") from None

    def _to_word(self, digits: List[int]) -> str:
        """
        Convert a list of digits to a string.

        :param digits: digits to convert.
        :returns: constructed string.
        """
        return "".join([self._alphabet[digit] for digit in digits])
