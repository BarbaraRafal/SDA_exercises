import unittest
from parameterized import parameterized


class TestSequence(unittest.TestCase):
    @parameterized.expand(
        (
                ("foo",),
                ["bar"],
                ["lee"],
                ["asdasd"],
        )
    )
    def test_01(self, asd):
        self.assertTrue(asd)

    @parameterized.expand(
        [
            ["foo", "a", "b", "1"],
            ["bar", "a", "b", "2"],
            ["lee", "b", "b", "3"],
        ]
    )
    def test_02(self, name, first_arg, second_arg, third_arg):
        print(third_arg)
        self.assertEqual(first_arg, "a")
