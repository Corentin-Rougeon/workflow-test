import unittest
from simplemath import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(1, 2)
        self.assertEqual(result, 3)

    def test_substraction(self):
        result = SimpleMath.substraction(1, 2)
        self.assertEqual(result,-1)