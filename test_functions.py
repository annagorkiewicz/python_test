from unittest import TestCase
from functions import divide, multiply


class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_result_approx(self):
        dividend = 15
        divisor = 3
        expected_result = 5
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 5
        expected_result = 0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_error_on_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_divide_error_on_zero_alternative(self):
        self.assertRaises(ValueError, lambda: divide(5, 0))

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected_result = 5
        self.assertEqual(multiply(expected_result), expected_result)

    def test_multiply_zero(self):
        expected_result = 0
        self.assertEqual(multiply(expected_result), expected_result)

    def test_multiply_result(self):
        inputs = (3, 5)
        expected_result = 15.0
        self.assertEqual(multiply(*inputs), expected_result)

    def test_multiply_input_with_zero(self):
        inputs = (3, 5, 0)
        expected_result = 0
        self.assertEqual(multiply(*inputs), expected_result)

    def test_multiply_negative(self):
        inputs = (-3, 5, 1)
        expected_result = -15.0
        self.assertEqual(multiply(*inputs), expected_result)

    def test_multiply_floats(self):
        inputs = (3.5, 2)
        expected_result = 7.0
        self.assertEqual(multiply(*inputs), expected_result)
