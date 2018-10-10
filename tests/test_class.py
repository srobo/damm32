"""Test that the class behaves as expected at a high level."""

from damm32 import Damm32


def test_class_instantiation():
    """Test that the class instantiates to an instance of Damm32."""
    d32 = Damm32()
    assert isinstance(d32, Damm32)
