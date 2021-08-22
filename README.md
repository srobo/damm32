# Damm32

[![Tests](https://github.com/pyinv/damm32/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/pyinv/damm32/actions/workflows/test.yml)

Python implementation of the Damm Algorithm in Base 32

By default, it uses an alphabet as specified in [RFC 4648](https://tools.ietf.org/html/rfc4648) which contains 32 alphanumeric characters, with similar looking characters removed. The padding symbol is not included.

## Installation

The package is available on [PyPI](https://pypi.org/project/damm32/) and can be installed using pip: `pip install damm32`

It is also available on the [Arch User Repository](https://aur.archlinux.org/packages/python-damm32/) as `python-damm32`.

Alternatively, you can clone the repository and use the module.

## Usage

The module contains a single class called `Damm32`, this class implements the methods for the checksum.

```
from damm32 import Damm32

d32 = Damm32()

digit = d32.calculate("HELLO")

d32.verify("HELLO" + digit)

```

You can also pass an list of length 32 to the constructor for the class to specify your alphabet.

```
from damm32 import Damm32

d32 = Damm32(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7'])

```

## How it works

This is an implementation of the [Damm Algorithm](https://en.wikipedia.org/wiki/Damm_algorithm) for use in Base 32 systems.

It will detect all occurrences of the two most frequently appearing types of transcription errors, namely altering one single digit, and transposing two adjacent digits (including the transposition of the trailing check digit and the preceding digit).

Since prepending leading zeros does not affect the check digit, variable length codes should not be verified together since, e.g., 0, 01, and 001, etc. produce the same check digit. However, all checksum algorithms are vulnerable to this.

The implementation uses a bitmask from [Table of Low-Weight Binary Irreducible Polynomials](https://www.hpl.hp.com/techreports/98/HPL-98-135.pdf) to enable calculation of the check digit without constructing the quasigroup.