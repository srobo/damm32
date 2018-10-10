# Damm32

[![CircleCI](https://circleci.com/gh/trickeydan/damm32.svg?style=svg)](https://circleci.com/gh/trickeydan/damm32)

Python implementation of the Damm Algorithm in Base 32

By default, it uses an alphabet as specified in [RFC 4648](https://tools.ietf.org/html/rfc4648) which contains 32 alphanumeric characters, with similar looking characters removed. The padding symbol is not included.

## Installation

The package is available on [PyPI](https://pypi.org/project/damm32/) and can be installed using pip.

`pip install damm32`

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