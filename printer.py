class PrinterError(RuntimeError):
    pass


class Printer:
    def __init__(self, pages_per_s: float, capacity: int):
        self._capacity = capacity
        self.pages_per_s = pages_per_s

    def print(self, pages):
        if pages > self._capacity:
            raise PrinterError('Printer does not have enough capacity to print all those pages.')

        self._capacity -= pages

        return f'Printed {pages} pages in {pages / self.pages_per_s:.2f} seconds.'
