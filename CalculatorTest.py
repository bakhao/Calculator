import unittest
from Calculator import calculate


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertAlmostEqual(calculate("2+3"), 5)

    def test_substract(self):
        self.assertAlmostEqual(calculate("5-3"), 2)

    def test_multiply(self):
        self.assertAlmostEqual(calculate("3*2"),6)

    def test_divide(self):
        self.assertAlmostEqual(calculate("10/2"),5)

    def test_operation_with_priority(self):
        self.assertAlmostEqual(calculate("10*2-3*4+4/2"), 10)

    def test_operator_power(self):
        self.assertAlmostEqual(calculate("2^4+5"), 21)

    def test_sqrt(self):
        self.assertAlmostEqual(calculate("sqrt(9)"), 3)

    def test_two_negative_numbers(self):
        self.assertAlmostEqual(calculate("-2+-3"), -5)