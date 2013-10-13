import unittest
from pymoqy.node import Node
from pymoqy.query import Query


class TestQuery(unittest.TestCase):

    def test_basic(self):
        q = Query()
        q.profile.username = 'test'
        print q()

if __name__ == '__main__':
    unittest.main()