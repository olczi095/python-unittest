import unittest
from employee.emp import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setting up...')
        self.emp = Employee('John', 'Smith', 80000)

    def tearDown(self):
        print('tearing down...')
        del self.emp

    def test_email(self):
        self.assertEqual(self.emp.email, 'john.smith@mail.com')

    def test_email_after_changing_first_name(self):
        self.emp.first_name = 'Adam'
        self.assertEqual(self.emp.email, 'adam.smith@mail.com')

    def test_email_after_changing_last_name(self):
        self.emp.last_name = 'Kowalski'
        self.assertEqual(self.emp.email, 'john.kowalski@mail.com')

    def test_tax(self):
        self.assertEqual(self.emp.tax, 13600)

    def test_salary_after_applying_bonus(self):
        self.emp.apply_bonus()
        self.assertEqual(self.emp.salary, 88000)
