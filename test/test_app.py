import os
from unittest import TestCase


class AppTest(TestCase):

    def test_main(self):
        result = os.system("python App.py")
        self.assertEqual(result, 0)
