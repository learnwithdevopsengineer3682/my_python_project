# tests/test_main.py

import unittest
from main import add_numbers, is_even

class TestMainFunctions(unittest.TestCase):

    def test_add_numbers(self):
        """Test that the add_numbers function returns the correct sum."""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_is_even(self):
        """Test that the is_even function correctly identifies even numbers."""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))

if __name__ == '__main__':
    unittest.main()
