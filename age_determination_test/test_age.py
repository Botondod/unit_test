import unittest
from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child_age(self):
        self.assertEqual(categorize_by_age(5), "Child")
        self.assertEqual(categorize_by_age(0), "Child")
        self.assertEqual(categorize_by_age(9), "Child")

    def test_teenager_age(self):
        self.assertEqual(categorize_by_age(10), "Teenager")
        self.assertEqual(categorize_by_age(15), "Teenager")
        self.assertEqual(categorize_by_age(18), "Teenager")

    def test_adult_age(self):
        self.assertEqual(categorize_by_age(19), "Adult")
        self.assertEqual(categorize_by_age(30), "Adult")
        self.assertEqual(categorize_by_age(64), "Adult")

    def test_golden_age(self):
        self.assertEqual(categorize_by_age(65), "Golden age")
        self.assertEqual(categorize_by_age(80), "Golden age")
        self.assertEqual(categorize_by_age(120), "Golden age")

    def test_invalid_age(self):
        self.assertEqual(categorize_by_age(-1), "Invalid age: -1")
        self.assertEqual(categorize_by_age(121), "Invalid age: 121")
        self.assertEqual(categorize_by_age(150), "Invalid age: 150")

# python -m unittest age_determination_test/test_age.py