import hashlib
import unittest
import datetime

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
        q.find = ((q.username == 'test') & ~(q.profile.gender == 1))
        self.assertDictEqual(q.find, {'$and': [{'username': {'$eq': 'test'}}, {'profile.gender': {'$not': {'$eq': 1}}}]})

    #example tests
    def test_example_1(self):
        q = Query()
        q.find = ((~(q.profile.age > 20)) & (q.username == 'test'))
        self.assertDictEqual(q.find, {'$and': [{'profile.age': {'$not': {'$gt': 20}}}, {'username': {'$eq': 'test'}}]})

    def test_example_2(self):
        q = Query()
        q.username = 'Sergey'
        q.profile.age = 28
        q.visits += 1
        self.assertDictEqual(q.update, {'$set': {'username': 'Sergey', 'profile.age': 28}, '$inc': {'visits': 1}})

    def test_example_3(self):
        q = Query()
        q.username = 'nikitinsm'
        q.password = hashlib.md5('password').hexdigest()
        q.profile.name = 'Sergey'
        q.profile.surname = 'Nikitin'
        q.profile.age = 28
        q.profile.gender = 'M'
        q.profile.dob = datetime.datetime(1985, 10, 8).strftime('%Y-%m-%d')
        q.created = 1381733783
        q.version += 1
        self.assertDictEqual(q.update, {'$set': {'username': 'nikitinsm', 'profile.name': 'Sergey', 'created': 1381733783, 'profile.age': 28, 'profile.surname': 'Nikitin', 'profile.gender': 'M', 'profile.dob': '1985-10-08', 'password': '5f4dcc3b5aa765d61d8327deb882cf99'}, '$inc': {'version': 1}})


if __name__ == '__main__':
    unittest.main()