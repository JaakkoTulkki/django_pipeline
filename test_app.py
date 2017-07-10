import unittest
from app import run

class TestApp(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(), 11)