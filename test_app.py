import unittest
from app import run

class TestApp(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(), 1)

    def test_nothing(self):
        self.assertTrue(True)
        self.assertTrue(True)
        self.assertTrue(True)