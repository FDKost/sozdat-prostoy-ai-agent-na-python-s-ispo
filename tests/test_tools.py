import pytest
from src.tools import get_current_time, add_numbers

def test_get_current_time():
    result = get_current_time()
    assert isinstance(result, str)
    assert result.endswith("Z")

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(2.5, 3.5) == 6.0
