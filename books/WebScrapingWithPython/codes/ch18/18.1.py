# 18.1.py
# Python unit test

import unittest


class TestAddition(unittest.TestCase):
    # Run before testing
    def setUp(self):
        print("Setting up the test")

    # Run after testing
    def tearDown(self):
        print("Tearing down the test")

    def test_twoPlusTwo(self):
        total = 2 + 2
        self.assertEqual(4, total)


if __name__ == "__main__":
    unittest.main()
