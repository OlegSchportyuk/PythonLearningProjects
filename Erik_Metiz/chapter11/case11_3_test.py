import unittest
from case11_3 import Employee

class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee."""
    def setUp(self) -> None:
        self.employee = Employee('Pandil', 'Lapikovich', 100000)
        self.salaries = [105000, 107000]

    def test_give_default_rise(self):
        """Проверяет метод give_raise по умолчанию."""
        self.employee.give_raise()
        self.assertIn(self.employee.year_salary, self.salaries)

    def test_give_custom_rise(self):
        """Проверяет метод give_rise с пользовательским значением."""
        self.employee.give_raise(7000)
        self.assertIn(self.employee.year_salary, self.salaries)

if __name__ == '__main__':
    unittest.main()