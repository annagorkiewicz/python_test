from unittest import TestCase
from printer import Printer, PrinterError


class TestPrinter(TestCase):
    def setUp(self):
        self.printer = Printer(pages_per_s=2.0, capacity=300)

    def test_print_within_capacity(self):
        message = self.printer.print(25)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(500)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 10
        expected_result = 'Printed 10 pages in 5.00 seconds.'
        result = self.printer.print(pages)
        self.assertEqual(result, expected_result)

    def test_print_speed_two_decimals(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected_result = 'Printed 11 pages in 3.67 seconds.'

        result = fast_printer.print(pages)
        self.assertEqual(result, expected_result)

    def test_print_multiple(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

    def test_print_multiple_runs_end_up_in_error(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

        with self.assertRaises(PrinterError):
            self.printer.print(1)
