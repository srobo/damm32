"""Test that the class behaves as expected at a high level."""

from tests.utils import random_string

from damm32 import Damm32


def test_empty_string():
    """Test empty strings."""
    d32 = Damm32()
    assert d32.verify("")
    assert d32.calculate("") == 'A'


def test_calculation_verifies():
    """Test that the calculated checkdigit passes verification."""
    d32 = Damm32()
    for i in range(1000):
        word = random_string(6)
        word += d32.calculate(word)
        print(word)
        assert d32.verify(word)


def test_known_good():
    """Test to see if known good strings pass verification."""
    data = [
        'HELLOW'
        'TFSI4JR',
        'JDLULAG',
        'BMQRZPX',
        'V6B4ORO',
        'BMRJXQ7',
        'LZYMFSV',
        '7JWZVIK',
        'UZI5F4A',
        'AWCWP3K',
        'PQCFBLJ',
        'T34OQKF',
        'LTEGIQO',
        'LMZFORD',
        'DWE67XD',
        'FUGDOJR',
        'O5BAULZ',
        'ZP5H5MK',
        'G3NZWI3',
        'FKXK7GX',
        'UETCW4P',
        'WRJ26DM',
        'VPYO6PP',
        'UFUBNW2',
    ]
    d32 = Damm32()
    for word in data:
        assert d32.verify(word)
