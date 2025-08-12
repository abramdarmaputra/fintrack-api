# tests/test_calc.py
from app.utils.calc import calculate_balance

def test_calculate_balance_positive():
    result = calculate_balance([1000, 2000], [500])
    assert result == 2500

def test_calculate_balance_negative():
    result = calculate_balance([500], [800])
    assert result == -300
