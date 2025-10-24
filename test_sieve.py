import pytest
from sievetools import *

def test_slow_interior():
    output = sieve_slow(10)
    expected = [2, 3, 5, 7]

    assert output == expected

def test_slow_two():
    output = sieve_slow(2)
    expected = [2]

    assert output == expected

def test_slow_one():
    output = sieve_slow(1)
    expected = []

    assert output == expected