import unittest
from calculator.calc_math import SimpleMathCalculator
from parameterized import parameterized


class TestSimpleMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMathCalculator()

    @parameterized.expand([
        ('positive', 3, 2, 5),
        ('mixed', -3, 2, -1),
        ('negative', -1, -1, -2),
        ('fail', 2, 3, 6)
    ])
    def test_add(self, name, x, y, result):
        self.assertEqual(self.calc.add(x, y), result)