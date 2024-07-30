from numb3rs import validate

def test_string():
    assert validate("cat") == False

def test_invalid():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False

def test_valid():
    assert validate("1.1.1.1") == True
