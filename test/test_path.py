import unittest
from pymoqy.path import Path


class TestPath(unittest.TestCase):

    def test_basic(self):
        p = Path()
        self.assertEquals(str(p.seg1.seg2.seg3), 'seg1.seg2.seg3')

    def test_gt(self):
        q = (Path().test > 1).data
        self.assertDictEqual(q, {'test': {'$gt': 1}})

    def test_gte(self):
        q = (Path().test >= 1).data
        self.assertDictEqual(q, {'test': {'$gte': 1}})

    def test_lt(self):
        q = (Path().test < 1).data
        self.assertDictEqual(q, {'test': {'$lt': 1}})

    def test_lte(self):
        q = (Path().test <= 1).data
        self.assertDictEqual(q, {'test': {'$lte': 1}})

    def test_eq(self):
        q = (Path().test == 1).data
        self.assertDictEqual(q, {'test': {'$eq': 1}})

    def test_mod(self):
        q = (Path().test % [4, 2]).data
        self.assertDictEqual(q, {'test': {'$mod': [4, 2]}})

    def test_in(self):
        q = (Path().test.s__in == [1, 2, 3]).data
        self.assertDictEqual(q, {'test': {'$in': [1, 2, 3]}})

    def test_not_in(self):
        q = (Path().test.s__nin == [1, 2, 3]).data
        self.assertDictEqual(q, {'test': {'$nin': [1, 2, 3]}})

if __name__ == '__main__':
    unittest.main()