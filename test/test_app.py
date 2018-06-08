import os
import unittest


class AppTest(unittest.TestCase):

    def test_main(self):
        result = os.system("python App.py")
        self.assertEqual(result, 0)
