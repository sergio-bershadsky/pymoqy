import unittest
from pymoqy.query import Query


class TestQuery(unittest.TestCase):

    def test_basic_update(self):
        q = Query()
        q.profile.username = 'test'
        self.assertDictEqual(q.update, {'$set': {'profile.username': 'test'}})

    def test_basic_inc(self):
        q = Query()
        q.some_counter += 1
        self.assertDictEqual(q.update, {'$inc': {'some_counter': 1}})

        q.some_counter -= 1
        self.assertDictEqual(q.update, {'$inc': {'some_counter': 0}})

    def test_basic_find(self):
        q = Query()
        q.find = ((q.username == 'test') & ~(q.profile.gender == 1))()
        self.assertDictEqual(q.find, {'$and': [{'username': {'$eq': 'test'}}, {'profile.gender': {'$not': {'$eq': 1}}}]})

    def test_slice(self):
        q = Query()
        q.find = q.array[1]()
        self.assertDictEqual(q.find, {'array': {'$slice': 1}})

    def test_slice_2(self):
        q = Query()
        q.find = q.array[1:10]()
        self.assertDictEqual(q.find, {'array': {'$slice': [1, 10]}})


if __name__ == '__main__':
    unittest.main()