import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(0.1 + 0.2, 0.3)

    def test_case_2(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3)

    def test_case_3(self):
        self.assertAlmostEqual(0.1234567, 0.1234567)

    def test_case_4(self):
        self.assertAlmostEqual(0.1234568, 0.1234567)

    def test_case_5(self):
        self.assertAlmostEqual(0.12332, 0.12345, 3)