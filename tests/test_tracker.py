import unittest
from octofit.tracker import start_tracker

class TestTracker(unittest.TestCase):
    def test_start(self):
        # This is a basic smoke test
        self.assertIsNone(start_tracker())

if __name__ == '__main__':
    unittest.main()