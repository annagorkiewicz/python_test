from unittest import TestCase
from functions import divide


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
