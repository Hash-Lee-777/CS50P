from bank import value

def test_zero():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0

def test_soso():
    assert value("How you doing?") == 20

def test_full():
    assert value("What's happening?") == 100
