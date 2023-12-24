# test_utils.py in the tests package
import unittest
from modules.utils import get_base_path

class TestUtils(unittest.TestCase):
    def test_get_base_path(self):
        self.assertTrue(isinstance(get_base_path(), str))

if __name__ == '__main__':
    unittest.main()
