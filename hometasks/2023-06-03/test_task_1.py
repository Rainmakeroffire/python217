import unittest

from task_1 import IntArrayHandler


class TestIntArrayHandler(unittest.TestCase):
    def setUp(self):
        self.obj_1 = IntArrayHandler([1, 3, -4])
        self.obj_2 = IntArrayHandler([])

    def test_get_sum(self):
        self.assertEqual(0, self.obj_1.get_sum())

    def test_get_mean(self):
        self.assertEqual(0, self.obj_1.get_mean())
        self.assertEqual('You passed an empty list', self.obj_2.get_mean())

    def test_get_max(self):
        self.assertEqual(3, self.obj_1.get_max())

    def test_get_min(self):
        self.assertEqual(-4, self.obj_1.get_min())


if __name__ == '__main__':
    unittest.main()
