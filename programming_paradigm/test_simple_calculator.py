
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-3, -6), 3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-4, -2), 8)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero

if __name__ == '__main__':
    unittest.main()
