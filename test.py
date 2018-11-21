import unittest

import main


class TestMain(unittest.TestCase):
    def test_say_hello(self):
        message = main.get_hello_message()
        self.assertEqual(message, 'hello world')

if __name__ == '__main__':
    unittest.main()
