import unittest
import re
from pymoqy.path import Path


class TestPath(unittest.TestCase):

    def test_basic(self):
        p = Path()
        self.assertEquals(str(p.seg1.seg2.seg3), 'seg1.seg2.seg3')

    def test_gt(self):
        q = (Path().test > 1)()
        self.assertDictEqual(q, {'test': {'$gt': 1}})

    def test_gte(self):
        q = (Path().test >= 1)()
        self.assertDictEqual(q, {'test': {'$gte': 1}})

    def test_lt(self):
        q = (Path().test < 1)()
        self.assertDictEqual(q, {'test': {'$lt': 1}})

    def test_lte(self):
        q = (Path().test <= 1)()
        self.assertDictEqual(q, {'test': {'$lte': 1}})

    def test_eq(self):
        q = (Path().test == 1)()
        self.assertDictEqual(q, {'test': {'$eq': 1}})

    def test_ne(self):
        q = (Path().test != 1)()
        self.assertDictEqual(q, {'test': {'$ne': 1}})

    def test_not(self):
        q = (~(Path().test == 1))()
        self.assertDictEqual(q, {'test': {'$not': {'$eq': 1}}})

    def test_mod(self):
        q = (Path().test % [4, 2])()
        self.assertDictEqual(q, {'test': {'$mod': [4, 2]}})

    def test_in(self):
        q = (Path().test.s__in == [1, 2, 3])()
        self.assertDictEqual(q, {'test': {'$in': [1, 2, 3]}})

    def test_not_in(self):
        q = (Path().test.s__nin == [1, 2, 3])()
        self.assertDictEqual(q, {'test': {'$nin': [1, 2, 3]}})

    def test_re(self):
        r = re.compile('[A-Za-z]+')
        q = (Path().test == r)()
        self.assertDictEqual(q, {'test': {'$regex': '[A-Za-z]+'}})

if __name__ == '__main__':
    unittest.main()