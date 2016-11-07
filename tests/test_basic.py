import unittest
from pymailer.helpers import *


class MyTest(unittest.TestCase):

    def test_get_event_returns_dict(self):
        self.assertEqual(type(get_event_data('{"test_key" : "test_value" }')), dict)

    def test_read_alerter_conf_file(self):
        self.assertEqual(type(read_alerter_conf_file('./test.json')), dict)


if __name__ == '__main__':
    unittest.main()
