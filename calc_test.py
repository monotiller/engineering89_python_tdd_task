import unittest
import pytest

from complicated_calc import ComplicatedCalc

class Calctest(unittest.TestCase):
    calc = ComplicatedCalc()

    def test_divisible(self):
        self.assertEqual(self.calc.divisible(2, 10), False)

    def test_modulus(self):
        self.assertEqual(self.calc.modulus(2, 2), 0)

    def test_positive(self):
        self.assertEqual(self.calc.positive(-6), False)