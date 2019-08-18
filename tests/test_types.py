"""Test that the class behaves as expected at a high level."""

import pytest
from damm32 import Damm32


def test_accepts_string() -> None:
    """Test that the calculate method accepts a string."""
    d32 = Damm32()
    d32.calculate("STRING")


def test_rejects_not_string() -> None:
    """Test that the calculate method rejects other types."""
    d32 = Damm32()
    with pytest.raises(TypeError):
        d32.calculate(3)  # type: ignore
