#This is the unit_tests file, used to check that the functions that I coded are giving the expected results.

import unittest
import random

from dec import incrementalNumber
from alpha import incrementalChar

class UnitTest(unittest.TestCase):
    def testDecimalCipher(self):
        self.assertEqual(incrementalNumber("123", 1) == [2,3,4], True)

    def testAlphaCipher(self):
        self.assertEqual(incrementalChar("abc", 1) == ['b','c','d'], True)

if __name__ == '__main__':
    unittest.main()