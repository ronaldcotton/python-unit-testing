# test_calc.py
# adapted from https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Unit-Testing/test_calc.py
# youtube: https://www.youtube.com/watch?v=6tNS--WetLI

# to run: python -m unittest test_calc.py

import unittest
import calc
import random
import sys

class TestCalc(unittest.TestCase):
    # all tests need to start with test_...(), otherwise not part of test suite.
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0) # edge
        self.assertEqual(calc.add(-1, -1), -2) # edge
        for i in range(100): # random cases
            x = random.randint(-(sys.maxsize-1), sys.maxsize)
            y = random.randint(-(sys.maxsize-1), sys.maxsize)
            self.assertEqual(calc.add(x, y), x+y)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
        for i in range(100):
            x = random.randint(-(sys.maxsize-1), sys.maxsize)
            y = random.randint(-(sys.maxsize-1), sys.maxsize)
            self.assertEqual(calc.subtract(x, y), x-y)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        for i in range(100):
            x = random.randint(-(sys.maxsize-1), sys.maxsize)
            y = random.randint(-(sys.maxsize-1), sys.maxsize)
            self.assertEqual(calc.multiply(x, y), x*y)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        for i in range(100):
            x = random.randint(-(sys.maxsize-1), sys.maxsize)
            y = random.randint(-(sys.maxsize-1), sys.maxsize)
            if y != 0:
                self.assertEqual(calc.divide(x, y), x/y)

        with self.assertRaises(ValueError): # divide-by-zero - check if error is raised.
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()