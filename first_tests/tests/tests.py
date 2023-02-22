import pytest
from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_calc(self):
        assert self.calc.adding(self, 2, 6) == 8

    def test_division_calc(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calc(self):
        assert self.calc.subtraction(self, 10, 2) == 8

    def test_multiplication_calc(self):
        assert self.calc.multiplication(self, 3, 4) == 12
