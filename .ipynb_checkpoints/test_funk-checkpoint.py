import pytest
from findfunk import funk

def test_normal_case():
    assert funk([1, 2, 3, 4, 3, 1, 2]) == 4

def test_negative_numbers():
    assert funk([-1, -1, -2]) == -2

def test_large_array():
    assert funk([1]*1000000 + [2]) == 2

def test_single_element():
    assert funk([5]) == 5

def test_invalid_input():
    with pytest.raises(ValueError):
        funk([1, 1, 2, 2])