import unittest


class FirstTestCase(unittest.TestCase):
    def test_passes(self):
        self.assertTrue(True)

    def test_fails(self):
        self.assertTrue(False)

    def test_something_to_test(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
