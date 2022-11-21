import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_incorrect_age_type_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 1000, 0.25, 'twenty')

    def test_calc_tax_second_incorrect_age_type_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 1000, 0.25, '20')

    def test_calc_tax_negative_age_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 1000, 0.25, -20)

    def test_calc_tax_zero_age_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 1000, 0.25, 0)

    def test_calc_tax_17_age_amount_lower_than_5000(self):
        self.assertEqual(calc_tax(20000, 0.1, 17), 2000)

    def test_calc_tax_17_age_amount_higher_than_5000(self):
        self.assertEqual(calc_tax(200000, 0.1, 17), 5000)

    def test_calc_tax_30_age_amount_lower_than_5000(self):
        self.assertEqual(calc_tax(20000, 0.1, 30), 2000)

    def test_calc_tax_30_age_amount_higher_than_5000(self):
        self.assertEqual(calc_tax(200000, 0.1, 30), 20000)

    def test_calc_tax_70_age_amount_lower_than_8000(self):
        self.assertEqual(calc_tax(20000, 0.1, 70), 2000)

    def test_calc_tax_70_age_amount_higher_than_8000(self):
        self.assertEqual(calc_tax(2000000, 0.1, 70), 8000)
