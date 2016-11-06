import unittest
import pymailer

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(list_to_string(['a', 'b', 'c']), 'abc')