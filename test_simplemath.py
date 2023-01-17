import unittest
from simplemath import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(3, 2)
        self.assertEqual(result, 3)