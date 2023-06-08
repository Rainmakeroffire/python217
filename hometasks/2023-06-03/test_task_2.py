import unittest

from task_2 import Number


class TestNumber(unittest.TestCase):
    def setUp(self):
        self.obj_1 = Number(5)
        self.obj_2 = Number('5')

    def test_set_value(self):
        self.assertEqual('Value updated', self.obj_1.set_value())

    def test_save(self):
        self.assertEqual('Saved successfully', self.obj_1.save())

    def test_load(self):
        self.assertEqual('Loaded successfully', self.obj_1.load())

    def test_make_oct(self):
        self.assertEqual('0o5', self.obj_1.make_oct())
        self.assertEqual('0o0', self.obj_2.make_oct())

    def test_make_hex(self):
        self.assertEqual('0x5', self.obj_1.make_hex())
        self.assertEqual('0x0', self.obj_2.make_hex())

    def test_make_bin(self):
        self.assertEqual('0b101', self.obj_1.make_bin())
        self.assertEqual('0b0', self.obj_2.make_bin())

    def test_make___str__(self):
        self.assertEqual('5', self.obj_1.__str__())
        self.assertEqual('0', self.obj_2.__str__())


if __name__ == '__main__':
    unittest.main()
