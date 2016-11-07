import unittest
from pymailer.helpers import *


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(type(get_event_data('{"test_key" : "test_value" }')), dict)