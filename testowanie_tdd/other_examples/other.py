import unittest


def setUpModule():
    print("setUpModule")


def tearDownModule():
    print("tearDownModule")


class FirstTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        self.x = "some string"
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_01(self):
        print("test_01")
        self.x = "changed string"
        print(self.x)
        self.assertEqual(self.x, "changed string")

    def test_02(self):
        print("test_02")
        print(self.x)
        self.assertEqual(self.x, "some string")
