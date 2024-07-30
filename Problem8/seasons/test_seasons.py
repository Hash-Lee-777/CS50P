from seasons import trans
from datetime import date

def test_get_minutes():
    assert trans(date(1999, 1, 1), date(2000, 1, 1)) == 525600
    assert trans(date(2001, 1, 1), date(2003, 1, 1)) == 1051200
    assert trans(date(1995, 1, 1), date(2000, 1, 1)) == 2629440
    assert trans(date(2020, 6, 1), date(2032, 1, 1)) == 6092640

