import unittest
from pymoqy.node import Node


class TestNode(unittest.TestCase):

    def test_and(self):
        n1 = Node(1)
        n2 = Node(2)
        query = (n1 & n2).data
        self.assertDictEqual({'$and': [1, 2]}, query)

    def test_or(self):
        n1 = Node(1)
        n2 = Node(2)
        query = (n1 | n2).data
        self.assertDictEqual({'$or': [1, 2]}, query)

    def test_invert(self):
        n1 = Node(1)
        query = (~n1).data
        self.assertDictEqual({'$not': 1}, query)

    def test_complex_1(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        query = (n1 | n2 & n3 | n4).data
        self.assertDictEqual({'$or': [1, {'$and': [2, 3]}, 4]}, query)

    def test_complex_2(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        query = ((n1 | n2) & (n3 | n4)).data
        self.assertDictEqual({'$and': [{'$or': [1, 2]}, {'$or': [3, 4]}]}, query)

    def test_complex_3(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        query = (n1 | ((n2 & n3) | n4)).data
        self.assertDictEqual({'$or': [1, {'$or': [{'$and': [2, 3]}, 4]}]}, query)

    def test_node_reuse(self):
        n1 = Node(1)
        n2 = Node(2)
        query = (n1 & n2).data
        self.assertDictEqual({'$and': [1, 2]}, query)
        query = (n1 | n2 & n1).data
        self.assertDictEqual({'$or': [1, {'$and': [2, 1]}]}, query)

    def test_node_reuse_2(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = n1 | n2
        n4 = n3 & n1
        query1 = (n1 & n2 | n3 & n4).data
        query2 = (n1 & n2 | (n1 | n2) & ((n1 | n2) & n1)).data
        self.assertDictEqual(query1, query2)


if __name__ == '__main__':
    unittest.main()