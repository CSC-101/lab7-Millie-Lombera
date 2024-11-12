import unittest
from convert import str_to_float

class TestCases(unittest.TestCase):
    def test_str_to_float1(self):
        self.assertEqual(str_to_float("10"),10)

    def test_str_to_float2(self):
        self.assertEqual(str_to_float("0"),0)

    def test_str_to_float3(self):
        self.assertEqual(str_to_float("hello"),None)