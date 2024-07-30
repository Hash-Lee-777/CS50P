from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("0/4") == 0
    assert convert("2/3") == 67
    with pytest.raises(ValueError):
        convert("two/three")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
     assert gauge(1) == "E"
     assert gauge(99) == "F"
     assert gauge(66) == "66%"
