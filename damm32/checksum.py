"""This file contains checksum implementations."""

from typing import List

Digit = int
DigitList = List[Digit]

class Damm32:
    """Implementation of the Damm algorithm."""

    BASE_SIZE = 32
    ALPHABET =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','2','3','4','5','6','7']

    def _calculate_from_digits(self, digits: DigitList) -> Digit:
        """Calculate the check digit from a list of integers."""
        mask = 37
        checkdigit = 0
        for digit in digits:
            checkdigit ^= digit
            checkdigit <<= 1
            if checkdigit >= Damm32.BASE_SIZE: 
                checkdigit ^= mask
        return checkdigit

    def _to_digits(self, word: str) -> DigitList:
        word.upper()
        dl = []
        for i in word:
            dl.append(Damm32.ALPHABET.index(i))
        return dl

    def _to_word(self, digits: DigitList) -> str:
        word = ""
        for i in digits:
            word.append(Damm32.ALPHABET[i])
        return word

    def calculate(self, word: str) -> str:
        digits = self._to_digits(word)
        checkdigit = self._calculate_from_digits(digits)
        return Damm32.ALPHABET[checkdigit]

    def verify(self, word: str) -> bool:
        return self.calculate(word) == Damm32.ALPHABET[0]
