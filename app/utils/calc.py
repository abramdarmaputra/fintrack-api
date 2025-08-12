# app/utils/calc.py
def calculate_balance(incomes: list[float], expenses: list[float]) -> float:
    return sum(incomes) - sum(expenses)
